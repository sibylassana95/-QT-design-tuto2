# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'carre.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 391, 80))
        self.widget.setStyleSheet("background-color: rgb(26, 95, 180);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(80, 10, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.btn_valider = QtWidgets.QPushButton(self.centralwidget)
        self.btn_valider.setGeometry(QtCore.QRect(50, 250, 271, 51))
        self.btn_valider.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 141, 102);\n"
"border-radius:5px")
        self.btn_valider.setObjectName("btn_valider")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 110, 361, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.n_nombre = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.n_nombre.setFont(font)
        self.n_nombre.setStyleSheet("color: rgb(26, 95, 180);")
        self.n_nombre.setObjectName("n_nombre")
        self.horizontalLayout.addWidget(self.n_nombre)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.resultat = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.resultat.setFont(font)
        self.resultat.setStyleSheet("color: rgb(0, 141, 102);")
        self.resultat.setObjectName("resultat")
        self.horizontalLayout.addWidget(self.resultat)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(10, 190, 381, 28))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.nombre = QtWidgets.QLineEdit(self.widget2)
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombre.setObjectName("nombre")
        self.horizontalLayout_2.addWidget(self.nombre)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Carre d\'un nombre"))
        self.btn_valider.setText(_translate("MainWindow", "Valider"))
        self.label_2.setText(_translate("MainWindow", "Le carre de "))
        self.n_nombre.setText(_translate("MainWindow", "N"))
        self.label_4.setText(_translate("MainWindow", "est"))
        self.resultat.setText(_translate("MainWindow", "resultat"))
        self.label_6.setText(_translate("MainWindow", "Entrez un nombre"))


