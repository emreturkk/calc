import math
from PyQt5.QtWidgets import (QApplication, QPushButton, QLineEdit, QVBoxLayout,
	QHBoxLayout,QSizePolicy, QWidget, QGridLayout, QLayout)
import sys
from PyQt5.QtCore import Qt


class hesap(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap Makinası")
        self.resize(100,300)
        
        
        
        #// Ekranda çıkacak kutucuk//#
        self.display = QLineEdit('0', self)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("qproperty-alignment: AlignRight;")
        self.display.setMaxLength(15)
        
        #//1. buton//#
        self.clear = QPushButton("C", self)
        
        self.bol = QPushButton("/", self)
        
        #//2. buton//#
        self.S7 = QPushButton("7")
        
        self.S8 = QPushButton("8", self)
        
        self.S9 = QPushButton("9", self)
        
        self.carp = QPushButton("*", self)
        
        #//3. buton//#
        self.S4 = QPushButton("4", self)
        
        self.S5 = QPushButton("5", self)
        
        self.S6 = QPushButton("6", self)
        
        self.cikar = QPushButton("-", self)
        
        #//4. buton//#
        self.S1 = QPushButton("1", self)
        
        self.S2 = QPushButton("2", self)
        
        self.S3 = QPushButton("3", self)
        
        self.topla = QPushButton("+", self)
        
        #//5.buton//#
        self.S0 = QPushButton("0", self)
        
        self.esit = QPushButton("=", self)
        self.back = QPushButton("Sil",self)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 4)
        mainLayout.addWidget(self.clear, 1, 0, 1, 2)
        mainLayout.addWidget(self.bol, 1, 2, 1, 2)
        mainLayout.addWidget(self.S7, 2, 0)

        mainLayout.addWidget(self.S8, 2, 1)
        mainLayout.addWidget(self.S9, 2, 2)
        mainLayout.addWidget(self.carp, 2, 3)
        mainLayout.addWidget(self.S4, 3, 0)

        mainLayout.addWidget(self.S5, 3, 1)
        mainLayout.addWidget(self.S6, 3, 2)
        mainLayout.addWidget(self.cikar, 3, 3)

        mainLayout.addWidget(self.S1, 4, 0)
        mainLayout.addWidget(self.S2, 4, 1)
        mainLayout.addWidget(self.S3, 4, 2)
        mainLayout.addWidget(self.topla, 4, 3)

        mainLayout.addWidget(self.S0, 5, 0, 1, 2)
        
        mainLayout.addWidget(self.back, 5, 2, 1, 1)
        mainLayout.addWidget(self.esit, 5, 3, 1,2)

        self.setLayout(mainLayout)
        

        
        
        
        
        
        
        
        
        
        
uygulama = QApplication(sys.argv)
pencere = hesap()
pencere.show()
uygulama.exec_()    