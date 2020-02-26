# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MY_YT_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_YouTubeVideoDownloader(object):
    def setupUi(self, YouTubeVideoDownloader):
        if YouTubeVideoDownloader.objectName():
            YouTubeVideoDownloader.setObjectName(u"YouTubeVideoDownloader")
        YouTubeVideoDownloader.resize(800, 600)
        self.centralwidget = QWidget(YouTubeVideoDownloader)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(390, 280, 75, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 70, 221, 131))
        self.label.setPixmap(QPixmap(u"../../../../Desktop/youtube.png"))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(60, 280, 291, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(510, 250, 71, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(610, 250, 71, 21))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(510, 280, 69, 22))
        self.comboBox.setEditable(True)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(610, 280, 69, 22))
        self.comboBox_2.setEditable(True)
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(60, 350, 291, 31))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(390, 350, 75, 31))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 400, 601, 111))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        YouTubeVideoDownloader.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(YouTubeVideoDownloader)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        YouTubeVideoDownloader.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(YouTubeVideoDownloader)
        self.statusbar.setObjectName(u"statusbar")
        YouTubeVideoDownloader.setStatusBar(self.statusbar)

        self.retranslateUi(YouTubeVideoDownloader)

        QMetaObject.connectSlotsByName(YouTubeVideoDownloader)
    # setupUi

    def retranslateUi(self, YouTubeVideoDownloader):
        YouTubeVideoDownloader.setWindowTitle(QCoreApplication.translate("YouTubeVideoDownloader", u"YouTube Downloader", None))
        self.pushButton.setText(QCoreApplication.translate("YouTubeVideoDownloader", u"Search", None))
        self.label.setText("")
        self.textEdit.setPlaceholderText(QCoreApplication.translate("YouTubeVideoDownloader", u"Paste video Url Here", None))
        self.label_2.setText(QCoreApplication.translate("YouTubeVideoDownloader", u"Select Format", None))
        self.label_3.setText(QCoreApplication.translate("YouTubeVideoDownloader", u"Select Quality", None))
        self.comboBox.setCurrentText(QCoreApplication.translate("YouTubeVideoDownloader", u"Video", None))
        self.comboBox_2.setCurrentText(QCoreApplication.translate("YouTubeVideoDownloader", u"480p", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("YouTubeVideoDownloader", u"Give the path", None))
        self.pushButton_2.setText(QCoreApplication.translate("YouTubeVideoDownloader", u"Browse...", None))
    # retranslateUi
if __name__ == "__main__":
        from PySide2 import *
        from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                                    QRect, QSize, QUrl, Qt)
        from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                                   QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                                   QRadialGradient)
        from PySide2.QtWidgets import *

        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_YouTubeVideoDownloader()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

