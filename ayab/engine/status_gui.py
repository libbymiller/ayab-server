# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'status_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QProgressBar, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)

class Ui_StatusTab(object):
    def setupUi(self, status_tab)->None:
        if not status_tab.objectName():
            status_tab.setObjectName(u"status_tab")
        self.verticalLayoutWidget_2 = QWidget(status_tab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, -1, 211, 333))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 16, 12, 6)
        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.progress_hall_l = QProgressBar(self.verticalLayoutWidget_2)
        self.progress_hall_l.setObjectName(u"progress_hall_l")
        self.progress_hall_l.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progress_hall_l.sizePolicy().hasHeightForWidth())
        self.progress_hall_l.setSizePolicy(sizePolicy1)
        self.progress_hall_l.setMaximum(1024)
        self.progress_hall_l.setValue(0)
        self.progress_hall_l.setAlignment(Qt.AlignCenter)
        self.progress_hall_l.setOrientation(Qt.Vertical)

        self.verticalLayout_6.addWidget(self.progress_hall_l, 0, Qt.AlignHCenter)

        self.label_hall_l = QLabel(self.verticalLayoutWidget_2)
        self.label_hall_l.setObjectName(u"label_hall_l")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_hall_l.sizePolicy().hasHeightForWidth())
        self.label_hall_l.setSizePolicy(sizePolicy2)
        self.label_hall_l.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_hall_l)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.progress_hall_r = QProgressBar(self.verticalLayoutWidget_2)
        self.progress_hall_r.setObjectName(u"progress_hall_r")
        self.progress_hall_r.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.progress_hall_r.sizePolicy().hasHeightForWidth())
        self.progress_hall_r.setSizePolicy(sizePolicy1)
        self.progress_hall_r.setMaximum(1024)
        self.progress_hall_r.setValue(0)
        self.progress_hall_r.setAlignment(Qt.AlignCenter)
        self.progress_hall_r.setOrientation(Qt.Vertical)

        self.verticalLayout_7.addWidget(self.progress_hall_r, 0, Qt.AlignHCenter)

        self.label_hall_r = QLabel(self.verticalLayoutWidget_2)
        self.label_hall_r.setObjectName(u"label_hall_r")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_hall_r.sizePolicy().hasHeightForWidth())
        self.label_hall_r.setSizePolicy(sizePolicy3)
        self.label_hall_r.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_hall_r)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(self.verticalLayoutWidget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.label_carriage = QLabel(self.verticalLayoutWidget_2)
        self.label_carriage.setObjectName(u"label_carriage")
        sizePolicy3.setHeightForWidth(self.label_carriage.sizePolicy().hasHeightForWidth())
        self.label_carriage.setSizePolicy(sizePolicy3)

        self.verticalLayout_4.addWidget(self.label_carriage, 0, Qt.AlignHCenter)

        self.slider_position = QSlider(self.verticalLayoutWidget_2)
        self.slider_position.setObjectName(u"slider_position")
        self.slider_position.setEnabled(False)
        self.slider_position.setMaximum(199)
        self.slider_position.setOrientation(Qt.Horizontal)
        self.slider_position.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_4.addWidget(self.slider_position)

        self.label_direction = QLabel(self.verticalLayoutWidget_2)
        self.label_direction.setObjectName(u"label_direction")
        sizePolicy2.setHeightForWidth(self.label_direction.sizePolicy().hasHeightForWidth())
        self.label_direction.setSizePolicy(sizePolicy2)
        self.label_direction.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_direction, 0, Qt.AlignHCenter)

        self.line_3 = QFrame(self.verticalLayoutWidget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.label_progress = QLabel(self.verticalLayoutWidget_2)
        self.label_progress.setObjectName(u"label_progress")
        font = QFont()
        font.setFamilies([u"Sans"])
        font.setPointSize(22)
        self.label_progress.setFont(font)
        self.label_progress.setMouseTracking(False)

        self.verticalLayout_4.addWidget(self.label_progress, 0, Qt.AlignHCenter)


        self.retranslateUi(status_tab)

        QMetaObject.connectSlotsByName(status_tab)
    # setupUi

    def retranslateUi(self, status_tab):
        self.label_8.setText(QCoreApplication.translate("StatusTab", u"Hall Sensors", None))
        self.progress_hall_l.setFormat(QCoreApplication.translate("StatusTab", u"%p%", None))
        self.label_hall_l.setText(QCoreApplication.translate("StatusTab", u"Hall Left", None))
        self.progress_hall_r.setFormat(QCoreApplication.translate("StatusTab", u"%p%", None))
        self.label_hall_r.setText(QCoreApplication.translate("StatusTab", u"Hall Right", None))
        self.label_7.setText(QCoreApplication.translate("StatusTab", u"Carriage", None))
        self.label_carriage.setText(QCoreApplication.translate("StatusTab", u"No carriage detected", None))
        self.label_direction.setText(QCoreApplication.translate("StatusTab", u"direction", None))
        self.label_9.setText(QCoreApplication.translate("StatusTab", u"Progress", None))
        self.label_progress.setText(QCoreApplication.translate("StatusTab", u"progress", None))
        pass
    # retranslateUi

