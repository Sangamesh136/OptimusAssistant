# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fdg.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Optimus(object):

    pushButton_2 = None
    pushButton = None

    def __init__(self):
        self.label=None
        self.centralwidget = None
        self.OptimusUi = None
        self.pushButton = None
        self.pushButton_2 = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OptimusUi = QtWidgets.QLabel(self.centralwidget)
        self.OptimusUi.setGeometry(QtCore.QRect(0, 0, 771, 581))
        self.OptimusUi.setStyleSheet("background-color: rgb(136, 0, 255);\n"
                                     "background-color: rgb(85, 0, 127);")
        self.OptimusUi.setText("")
        self.OptimusUi.setPixmap(QtGui.QPixmap("C:/Users/sanga/Downloads/Siri.gif"))
        self.OptimusUi.setScaledContents(True)
        self.OptimusUi.setObjectName("OptimusUi")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 771, 581))
        self.label.setStyleSheet("background-color: rgb(136, 0, 255);\n"
                                 "background-color: rgb(85, 0, 127);")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 480, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(242, 203, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 520, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(206, 254, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(240, 480, 291, 61))
        self.textBrowser.setStyleSheet("background:transparent;\n"
                                       "border-radius:none;\n"
                                       "font-size:12px;")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Optimus()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# from PyQt5 import QtCore, QtGui, QtWidgets
#
#
# class Ui_Optimus(object):
#     pushButton_2 = None
#     pushButton = None
#     label = None  # Add this line to declare label
#
#     def __init__(self):
#         self.label = None
#         self.centralwidget = None
#         self.OptimusUi = None
#         self.pushButton = None
#         self.pushButton_2 = None
#
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(766, 579)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#
#         self.OptimusUi = QtWidgets.QLabel(self.centralwidget)
#         self.OptimusUi.setGeometry(QtCore.QRect(0, 0, 771, 581))
#         self.OptimusUi.setStyleSheet("background-color: rgb(136, 0, 255);\n"
#                                      "background-color: rgb(85, 0, 127);")
#         self.OptimusUi.setText("")
#         self.OptimusUi.setPixmap(QtGui.QPixmap("C:/Users/sanga/Downloads/Siri.gif"))
#         self.OptimusUi.setScaledContents(True)
#         self.OptimusUi.setObjectName("OptimusUi")
#
#         self.label = QtWidgets.QLabel(self.centralwidget)  # Add this line to create label
#         self.label.setGeometry(QtCore.QRect(10, 10, 100, 20))  # Adjust the position and size as needed
#         self.label.setText("OPTIMUS")  # Set the text for the label
#         self.label.setObjectName("label")
#
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(630, 480, 91, 31))
#         font = QtGui.QFont()
#         font.setPointSize(11)
#         self.pushButton.setFont(font)
#         self.pushButton.setStyleSheet("background-color: rgb(242, 203, 255);")
#         self.pushButton.setObjectName("pushButton")
#
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(630, 520, 91, 31))
#         font = QtGui.QFont()
#         font.setPointSize(11)
#         self.pushButton_2.setFont(font)
#         self.pushButton_2.setStyleSheet("background-color: rgb(206, 254, 255);")
#         self.pushButton_2.setObjectName("pushButton_2")
#
#         self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
#         self.textBrowser.setGeometry(QtCore.QRect(240, 480, 291, 61))
#         self.textBrowser.setStyleSheet("background:transparent;\n"
#                                        "border-radius:none;\n"
#                                        "font-size:12px;")
#         self.textBrowser.setObjectName("textBrowser")
#
#         MainWindow.setCentralWidget(self.centralwidget)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.pushButton.setText(_translate("MainWindow", "Run"))
#         self.pushButton_2.setText(_translate("MainWindow", "Exit"))
#
#
# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Optimus()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())