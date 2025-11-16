# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_gui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QLabel, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)
class Ui_Options(object):
    def setupUi(self, options_tab)->None:
        if not options_tab.objectName():
            options_tab.setObjectName(u"options_tab")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(options_tab.sizePolicy().hasHeightForWidth())
        options_tab.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(options_tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 244, 414))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 20, 12, 20)
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.knitting_mode_box = QComboBox(self.verticalLayoutWidget)
        self.knitting_mode_box.setObjectName(u"knitting_mode_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.knitting_mode_box.sizePolicy().hasHeightForWidth())
        self.knitting_mode_box.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.knitting_mode_box)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.color_edit = QSpinBox(self.verticalLayoutWidget)
        self.color_edit.setObjectName(u"color_edit")
        sizePolicy1.setHeightForWidth(self.color_edit.sizePolicy().hasHeightForWidth())
        self.color_edit.setSizePolicy(sizePolicy1)
        self.color_edit.setMinimum(2)
        self.color_edit.setMaximum(6)

        self.verticalLayout_3.addWidget(self.color_edit)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.start_row_edit = QSpinBox(self.verticalLayoutWidget)
        self.start_row_edit.setObjectName(u"start_row_edit")
        sizePolicy1.setHeightForWidth(self.start_row_edit.sizePolicy().hasHeightForWidth())
        self.start_row_edit.setSizePolicy(sizePolicy1)
        self.start_row_edit.setMinimum(1)
        self.start_row_edit.setMaximum(99999)

        self.verticalLayout_3.addWidget(self.start_row_edit)

        self.inf_repeat_checkbox = QCheckBox(self.verticalLayoutWidget)
        self.inf_repeat_checkbox.setObjectName(u"inf_repeat_checkbox")
        sizePolicy1.setHeightForWidth(self.inf_repeat_checkbox.sizePolicy().hasHeightForWidth())
        self.inf_repeat_checkbox.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.inf_repeat_checkbox)

        self.gbox_startneedle = QGroupBox(self.verticalLayoutWidget)
        self.gbox_startneedle.setObjectName(u"gbox_startneedle")
        self.gbox_startneedle.setMinimumSize(QSize(224, 52))
        self.gbox_startneedle.setFlat(False)
        self.start_needle_color = QComboBox(self.gbox_startneedle)
        self.start_needle_color.setObjectName(u"start_needle_color")
        self.start_needle_color.setGeometry(QRect(60, 20, 165, 32))
        self.start_needle_edit = QSpinBox(self.gbox_startneedle)
        self.start_needle_edit.setObjectName(u"start_needle_edit")
        self.start_needle_edit.setGeometry(QRect(0, 20, 60, 32))
        self.start_needle_edit.setMinimum(1)
        self.start_needle_edit.setMaximum(100)
        self.start_needle_edit.setValue(20)

        self.verticalLayout_3.addWidget(self.gbox_startneedle)

        self.gbox_stopneedle = QGroupBox(self.verticalLayoutWidget)
        self.gbox_stopneedle.setObjectName(u"gbox_stopneedle")
        self.gbox_stopneedle.setMinimumSize(QSize(224, 52))
        self.stop_needle_color = QComboBox(self.gbox_stopneedle)
        self.stop_needle_color.setObjectName(u"stop_needle_color")
        self.stop_needle_color.setGeometry(QRect(60, 20, 165, 32))
        self.stop_needle_edit = QSpinBox(self.gbox_stopneedle)
        self.stop_needle_edit.setObjectName(u"stop_needle_edit")
        self.stop_needle_edit.setGeometry(QRect(0, 20, 60, 32))
        self.stop_needle_edit.setMinimum(1)
        self.stop_needle_edit.setMaximum(100)
        self.stop_needle_edit.setValue(20)

        self.verticalLayout_3.addWidget(self.gbox_stopneedle)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.alignment_combo_box = QComboBox(self.verticalLayoutWidget)
        self.alignment_combo_box.setObjectName(u"alignment_combo_box")
        sizePolicy1.setHeightForWidth(self.alignment_combo_box.sizePolicy().hasHeightForWidth())
        self.alignment_combo_box.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.alignment_combo_box)

        self.auto_mirror_checkbox = QCheckBox(self.verticalLayoutWidget)
        self.auto_mirror_checkbox.setObjectName(u"auto_mirror_checkbox")
        sizePolicy1.setHeightForWidth(self.auto_mirror_checkbox.sizePolicy().hasHeightForWidth())
        self.auto_mirror_checkbox.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.auto_mirror_checkbox)

        self.auto_mirror_icon = QLabel(self.verticalLayoutWidget)
        self.auto_mirror_icon.setObjectName(u"auto_mirror_icon")
        self.auto_mirror_icon.setFixedSize(QSize(59, 64))

        self.verticalLayout_3.addWidget(self.auto_mirror_icon)

        self.continuous_reporting_checkbox = QCheckBox(self.verticalLayoutWidget)
        self.continuous_reporting_checkbox.setObjectName(u"continuous_reporting_checkbox")

        self.verticalLayout_3.addWidget(self.continuous_reporting_checkbox)


        self.retranslateUi(options_tab)

        QMetaObject.connectSlotsByName(options_tab)
    # setupUi

    def retranslateUi(self, options_tab):
        self.label_4.setText(QCoreApplication.translate("Options", u"Knitting Mode", None))
        self.label_6.setText(QCoreApplication.translate("Options", u"Colors", None))
        self.label_5.setText(QCoreApplication.translate("Options", u"Start Row", None))
        self.start_row_edit.setSuffix("")
        self.start_row_edit.setPrefix("")
        self.inf_repeat_checkbox.setText(QCoreApplication.translate("Options", u"Infinite Repeat", None))
        self.gbox_startneedle.setTitle(QCoreApplication.translate("Options", u"Start Needle", None))
        self.start_needle_edit.setPrefix("")
        self.gbox_stopneedle.setTitle(QCoreApplication.translate("Options", u"Stop Needle", None))
        self.stop_needle_edit.setPrefix("")
        self.label_3.setText(QCoreApplication.translate("Options", u"Alignment", None))
        self.auto_mirror_checkbox.setText(QCoreApplication.translate("Options", u"Knit Side Image", None))
        self.continuous_reporting_checkbox.setText(QCoreApplication.translate("Options", u"Continuous Status Reporting", None))
        pass
    # retranslateUi

