# ayab-server

A hacked around versio of AYAB-desktop to send single lines using a web server and curl

It's pretty messy. I made it using an Arduino and no shield - using https://github.com/AllYarnsAreBeautiful/ayab-firmware using 
the debug button - https://github.com/search?q=repo%3AAllYarnsAreBeautiful%2Fayab-firmware+DBG_BTN_PIN&type=code

i.e. in board.h

    #define DBG_NOMACHINE 1

I haven't tested it with a real machine


# Usage

## Run the server:

plug in the arduino and then

    python server.py


## Send a line and start the knitting:

    curl http://localhost:5000/send_line_and_knit?line=0101010

0 is black and 1 is white. It stops automatically at the end

## test - send a random line

    curl http://localhost:5000/send_random

You need to call start_knitting after

## Send a line of 0 and 1

    curl http://localhost:5000/send_line?line=0101010

0 is black and 1 is white. You need to call start_knitting after

## start knitting

    curl http://localhost:5000/start_knitting

it stops automatically at the end

## load an image from a post request

    curl -X POST http://localhost:5000/load_image -d image=/Users/libby/ayab-server/patterns/stirnband_160x20.png

You need to call start_knitting after
