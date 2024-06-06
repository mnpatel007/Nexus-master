from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Nexus 2.0")
        MainWindow.resize(540, 540)  # Resize the main window
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 540, 540))  # Resize and position the label
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Nexus/utils/images/nexus.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 460, 91, 31))  # Position the button
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 460, 91, 31))  # Position the button
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 0, 0);\n"
                                        "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 261, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Nexus/utils/images/initiating.gif"))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(270, 20, 131, 31))  # Position the text browser
        self.textBrowser.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                       "background-color:transparent;\ncolor:white;"
                                       "border-radius:none;\n"
                                       "")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(410, 20, 131, 31))  # Position the text browser
        self.textBrowser_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                         "background-color:transparent;\ncolor:white;"
                                         "border-radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 150, 240, 240))  # Center the third label
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Nexus/utils/images/a15hko.gif"))
        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 26))  # Adjust menubar size
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nexus"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())