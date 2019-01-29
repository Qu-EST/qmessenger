# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/quest/Documents/codes/qc/qc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QMessenger(object):
    def setupUi(self, QMessenger):
        self.messages = []
        QMessenger.setObjectName("QMessenger")
        QMessenger.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(QMessenger)
        self.centralwidget.setObjectName("centralwidget")
        self.MessageArea = QtWidgets.QScrollArea(self.centralwidget)
        self.MessageArea.setGeometry(QtCore.QRect(20, 90, 761, 391))
        self.MessageArea.setWidgetResizable(True)
        self.MessageArea.setObjectName("MessageArea")
        self.vbar = self.MessageArea.verticalScrollBar()
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 759, 389))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MessageArea.setWidget(self.scrollAreaWidgetContents)
        self.ToSendText = QtWidgets.QLineEdit(self.centralwidget)
        self.ToSendText.setGeometry(QtCore.QRect(20, 500, 641, 31))
        self.ToSendText.setObjectName("ToSendText")
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendButton.setGeometry(QtCore.QRect(680, 500, 91, 31))
        self.SendButton.setObjectName("SendButton")
        QMessenger.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QMessenger)
        self.statusbar.setObjectName("statusbar")
        QMessenger.setStatusBar(self.statusbar)
        self.flipper = True

        self.retranslateUi(QMessenger)
        QtCore.QMetaObject.connectSlotsByName(QMessenger)

        self.SendButton.clicked.connect(self.addLabel)

    def retranslateUi(self, QMessenger):
        _translate = QtCore.QCoreApplication.translate
        QMessenger.setWindowTitle(_translate("QMessenger", "QMessenger"))
        self.SendButton.setText(_translate("QMessenger", "PushButton"))

    def addLabel(self):
        _translate = QtCore.QCoreApplication.translate
        textvalue = self.ToSendText.text()
        self.ToSendText.setText("")
        messages_n=QtWidgets.QLabel(self.scrollAreaWidgetContents)
        messages_n.setMinimumSize(QtCore.QSize(20, 20))
        messages_n.setMaximumSize(QtCore.QSize(500, 20))
        messages_n.setScaledContents(True)
        messages_n.setObjectName("MessageLabel"+str(len(self.messages)))

        messages_n.setStyleSheet("""
        .QLabel {
            border: 2px solid black;
            border-radius: 5px;            
            }
        """)
        if self.flipper:
            self.verticalLayout.addWidget(messages_n, 0, QtCore.Qt.AlignRight)
            messages_n.setAlignment(QtCore.Qt.AlignRight) 
            self.flipper = False
        else:
            self.verticalLayout.addWidget(messages_n, 0, QtCore.Qt.AlignLeft)
            messages_n.setAlignment(QtCore.Qt.AlignLeft)
            self.flipper = True

        messages_n.setText(_translate("QMessenger", textvalue))
        self.messages.append(messages_n)
        self.vbar.setValue(self.vbar.maximum()+20)
        #self.MessageArea.ensureVisible()
        

    def keyPressEvent(self, enter):
        if (enter.key() == QtCore.Qt.Key_Enter) or (enter.key() ==16777220) :
            self.addLabel()
        
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_QMessenger()
    MainWindow.keyPressEvent=ui.keyPressEvent
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


