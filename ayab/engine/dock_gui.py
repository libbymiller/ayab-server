# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dock_gui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QGroupBox,
    QHBoxLayout, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Dock(object):
    def setupUi(self, DockWidget)->None:
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dock_child = QWidget()
        self.dock_child.setObjectName(u"dock_child")
        self.dock_child.setGeometry(QRect(0, 0, 240, 506))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dock_child.sizePolicy().hasHeightForWidth())
        self.dock_child.setSizePolicy(sizePolicy)
        self.dock_child.setMinimumSize(QSize(240, 506))
        self.dock_child.setMaximumSize(QSize(260, 506))
        self.ayab_config = QWidget(self.dock_child)
        self.ayab_config.setObjectName(u"ayab_config")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ayab_config.sizePolicy().hasHeightForWidth())
        self.ayab_config.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.ayab_config)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.ayab_config)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(240, 0))
        self.groupBox.setMaximumSize(QSize(240, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.serial_port_dropdown = QComboBox(self.groupBox)
        self.serial_port_dropdown.setObjectName(u"serial_port_dropdown")

        self.horizontalLayout_3.addWidget(self.serial_port_dropdown)

        self.refresh_ports_button = QPushButton(self.groupBox)
        self.refresh_ports_button.setObjectName(u"refresh_ports_button")

        self.horizontalLayout_3.addWidget(self.refresh_ports_button)


        self.verticalLayout.addWidget(self.groupBox)

        self.tab_widget = QTabWidget(self.ayab_config)
        self.tab_widget.setObjectName(u"tab_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy3)
        self.tab_widget.setMinimumSize(QSize(220, 430))
        self.tab_widget.setMaximumSize(QSize(1000000, 16777215))
        self.tab_widget.setDocumentMode(False)
        self.tab_widget.setTabBarAutoHide(False)

        self.verticalLayout.addWidget(self.tab_widget)

        DockWidget.setWidget(self.dock_child)

        self.retranslateUi(DockWidget)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle("")
        self.groupBox.setTitle(QCoreApplication.translate("Dock", u"Port Selection", None))
        self.refresh_ports_button.setText(QCoreApplication.translate("Dock", u"Refresh", None))
    # retranslateUi

