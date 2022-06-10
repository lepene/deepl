# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Gdrive\Jll\Documents\Python\Deepl\f1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_f1(object):
    def setupUi(self, f1):
        # initialiser la fenêtre
        f1.setObjectName("f1")
        f1.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(f1)
        self.centralwidget.setObjectName("centralwidget")
        # placer le label compteur d'utilisation, en haut
        self.labelUtilisation = QtWidgets.QLabel(self.centralwidget)
        self.labelUtilisation.setGeometry(QtCore.QRect(40, 10, 421, 31))
        self.labelUtilisation.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelUtilisation.setText("")
        self.labelUtilisation.setObjectName("labelUtilisation")
        # placer la zone de texte source, en dessous
        self.sourceText = QtWidgets.QPlainTextEdit(self.centralwidget)
        x = 30
        y = 80
        w = 630
        h = 171
        self.sourceText.setGeometry(QtCore.QRect(x, y, w, h))
        self.sourceText.setObjectName("sourceText")
        # placer le boutton Traduire, en dessous
        y = y + h + 10
        self.buttonTraduire = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTraduire.setGeometry(QtCore.QRect(x + (w / 2) - 30, y, 100, 30))
        self.buttonTraduire.setObjectName("buttonTraduire")
        # placer la zone de texte cible, en dessous
        y = y + 30 + 10
        self.cibleText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.cibleText.setGeometry(QtCore.QRect(x, y, w, h))
        self.cibleText.setObjectName("cibleText")
        # finaliser
        f1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(f1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        f1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(f1)
        self.statusbar.setObjectName("statusbar")
        f1.setStatusBar(self.statusbar)

        self.retranslateUi(f1)
        QtCore.QMetaObject.connectSlotsByName(f1)

    def retranslateUi(self, f1):
        _translate = QtCore.QCoreApplication.translate
        f1.setWindowTitle(_translate("f1", "Traducteur Deepl"))
        self.buttonTraduire.setText(_translate("f1", "Traduire"))
