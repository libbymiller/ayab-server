import sys
import os
import logging
import random
import numpy as np
from PIL import Image
import json

from ayab import utils
from flask import Flask 
from flask import request

from ayab.gui_fsm import gui_fsm

from ayab.signal_sender import SignalSender
from ayab.signal_receiver import SignalReceiver
from ayab.preferences import Preferences

from ayab.thread import GenericThread
from ayab.engine import Engine
from ayab.engine.engine_fsm import Operation

from ayab.image import AyabImage
from ayab.engine.pattern import Pattern

from ayab.audio import AudioPlayer

class MyAPI(SignalSender):

    # most of the non-gui stuff from ayab.py
    def init(self, parent: SignalReceiver):

        self.signal_receiver = SignalReceiver()

        # get preferences
        self.settings = None
        with open('preferences.json', 'r') as file:
           self.settings = json.load(file)

        self.prefs = Preferences(self)

        #self.about: About = About(self)

        self.engine: Engine = Engine(self) # we def need this though, removed ui bits

        #self.knitprog = KnitProgress(self) # mostly ui?? 😬
        self.audio = AudioPlayer(self)

        self.knit_thread = GenericThread(self.engine.run, Operation.KNIT)

        # Activate signals (these are really important)
        self.signal_receiver.activate_signals(self)

        # initialize FSM (finite state machine)
        self.fsm = gui_fsm()
        self.fsm.set_transitions(self)
        self.fsm.set_properties(self)
        self.fsm.machine.start()


# method to generate an image
# expects an array of rows like this [[0,1,1,0]]

    def generate_image(self,array_of_rows):
        new_arr = []
        w = 0
        h = 0

        # build a new array ensuring ints, and get width and height
        for r in array_of_rows:
           new_r = []
           for p in r:
              try:
                 int(p)
                 new_r.append(int(p))
              except ValueError:
                 pass
           new_arr.append(new_r)
           h = len(new_r)

        w = len(array_of_rows)
        print("w",w,"h",h)
        numpy_csv = np.array(new_arr).astype("float")
        numpy_csv = numpy_csv.reshape((w,h)).astype('uint8')*255
        print(numpy_csv)
        img = Image.fromarray(numpy_csv,mode='L')
        img.show()
        return img

# load an image from a post request
# curl -X POST http://localhost:5000/load_image -d image=/Users/libby/knitting/ayab/main/patterns/stirnband_160x20.png
# need to call start_knitting after

    def load_image(self, img_fn) -> None:
        attributes = dir(self)
        img = AyabImage(self)
        img.filename = img_fn
        img.open(img.filename)
        print("config",self.engine.config)
        pattern = Pattern(img.image, self.engine.config, self.engine.config.num_colors)
        self.engine.knit_config(img.image)

# test - send a random line
# curl http://localhost:5000/send_random
# need to call start_knitting after

    def send_random(self) -> None:
        img = AyabImage(self)# hmm
        # generate a random line of (for now) 10
        arr = [0,0,0,0,0,1,1,1,1,1]
        random.shuffle(arr)
        # create an image from that
        out = self.generate_image([arr])
        print("out width",out.width)
        img.image = out
        pattern = Pattern(img.image, self.engine.config, self.engine.config.num_colors)
        self.engine.knit_config(img.image)
        return str(arr)

# send a line of 0 and 1
# 0 is black and 1 is white
# curl http://localhost:5000/send_line?line=0101010
# need to call start_knitting after

    def send_line(self, line) -> str:

        img = AyabImage(self)# hmm
        arr = list(line)
        # cast string to int
        arr = list(map(int, arr))
        print("arr1",arr)
        out = self.generate_image([arr])
        img.image = out
        #out.save("rotated.jpg")
        pattern = Pattern(img.image, self.engine.config, self.engine.config.num_colors)
        self.engine.knit_config(img.image)
        return str(arr)

# start knitting
# curl http://localhost:5000/start_knitting
# it stops automatically at the end

    def start_knitting(self) -> None:
        """Start the knitting process."""

        self.emit_knit_triggered()
        self.start_operation()
        # reset knit progress window
        #self.knitprog.start()
        # start thread for knit engine   
        self.knit_thread.start()  

# send a line and start the knitting
# curl http://localhost:5000/send_line_and_knit?line=0101010
# it stops automatically at the end

    def send_line_and_knit(self, line) -> None:
        self.send_line(line)
        self.start_knitting()


# this did UI stuff
    def start_operation(self) -> None:
        pass

    def finish_operation(self, operation: Operation) -> None:
        if operation == Operation.KNIT:
            self.knit_thread.wait()

    def set_image_dimensions(self) -> None:
        """Set dimensions of image."""
        width, height = self.scene.ayabimage.image.size
        self.engine.config.update_needles()  # in case machine width changed
        self.engine.config.set_image_dimensions(width, height)
        print("setting image dimensions".self.engine.status)

    def update_start_row(self, start_row: int) -> None:
        self.scene.row_progress = start_row
        self.engine.status.current_row = start_row
        print("updating start row",self.engine.status)

    def notify(self, text: str, log: bool = True) -> None:
        """Update the notification field."""
        if log:
            print("LOGGING from notify")
            logging.info("Notification: " + text)
        else:
            print("no log",log)

    def configure_logger(self) -> None:
        cwd = os.getcwd()
        logfile = os.path.join(cwd, "ayab_log.txt")
        logging.basicConfig(
            filename=logfile,
            level=logging.INFO,
            format="%(asctime)s %(name)-8s %(levelname)-8s %(message)s",
            datefmt="%y-%m-%d %H:%M:%S",
        )
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(
            logging.Formatter("%(asctime)s %(name)-8s %(levelname)-8s %(message)s")
        )
        logging.getLogger().addHandler(console)

    def run(self):
        app = Flask('MyAPI')

        doc = """
<html>
<pre>
# send a line and start the knitting
# 0 is black and 1 is white
# curl http://localhost:5000/send_line_and_knit?line=0101010
# it stops automatically at the end

# test - send a random line
# curl http://localhost:5000/send_random
# need to call start_knitting after

# send a line of 0 and 1
# 0 is black and 1 is white
# curl http://localhost:5000/send_line?line=0101010
# need to call start_knitting after

# start knitting
# curl http://localhost:5000/start_knitting
# it stops automatically at the end

# load an image from a post request
# curl -X POST http://localhost:5000/load_image -d image=/Users/libby/knitting/ayab/main/patterns/stirnband_160x20.png
# need to call start_knitting after
</pre>
</html>
        """

        @app.route('/')
        def hello():
          return doc

        @app.route('/load_image', methods = ['POST'])
        def load_image():
          if request.method == 'POST':
            data = request.form
            print("data",data)
            self.load_image(data["image"])
            return 'load_image'

        @app.route('/send_random')
        def send_random():
          line_str = self.send_random()
          return line_str

        @app.route('/send_line')
        def send_line():
          line = request.args.get('line')
          line_str = self.send_line(line)
          return line

        @app.route('/start_knitting')
        def start_knitting():
          self.start_knitting()
          return 'Starting knitting'

        @app.route('/send_line_and_knit')
        def send_line_and_knit():
          line = request.args.get('line')
          line_str = self.send_line_and_knit(line)
          return line

        #app.run(debug = True)
        app.run()


if __name__ == "__main__":
    sr = SignalReceiver()
    app = MyAPI(sr) 
    app.init(sr)
    app.run()

