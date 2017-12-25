from PyQt5.QtWidgets import *
import sys

class hesap(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap Makinası")
        self.resize(100,300)
        
        
        #///Layout başlangıcı///#
        self.layoutAna = QVBoxLayout(self)
        self.layoutMetin = QVBoxLayout(self)
        
        self.layout2 = QHBoxLayout(self)
        self.layoutClear = QVBoxLayout(self)
        self.layoutBol = QVBoxLayout(self)
        
        self.layoutRakam1 = QHBoxLayout(self)
        self.layoutS7 = QVBoxLayout(self)
        self.layoutS8 = QVBoxLayout(self)
        self.layoutS9 = QVBoxLayout(self)
        self.layoutCarp = QVBoxLayout(self)
        
        self.layoutRakam2 = QHBoxLayout(self)
        self.layoutS4 = QVBoxLayout(self)
        self.layoutS5 = QVBoxLayout(self)
        self.layoutS6 = QVBoxLayout(self)
        self.layoutCikar = QVBoxLayout(self)
        
        self.layoutRakam3 = QHBoxLayout(self)
        self.layoutS1 = QVBoxLayout(self)
        self.layoutS2 = QVBoxLayout(self)
        self.layoutS3 = QVBoxLayout(self)
        self.layoutTopla = QVBoxLayout(self)
        
        self.layoutRakam4 = QHBoxLayout(self)
        self.layoutS0 = QVBoxLayout(self)
        self.layoutEsit = QVBoxLayout(self)
        
        
        #// Ekranda çıkacak kutucuk//#
        self.metin = QListWidget(self)
        self.metin.setGeometry(150,0,300,40)
        #//1. buton//#
        self.clear = QPushButton("C")
        
        self.bol = QPushButton(self)
        self.bol.setText("/")
        #//2. buton//#
        self.S7 = QPushButton("7")
        
        self.S8 = QPushButton(self)
        self.S8.setText("8")
        self.S9 = QPushButton(self)
        self.S9.setText("9")
        self.carp = QPushButton(self)
        self.carp.setText("*")
        #//3. buton//#
        self.S4 = QPushButton(self)
        self.S4.setText("4")
        self.S5 = QPushButton(self)
        self.S5.setText("5")
        self.S6 = QPushButton(self)
        self.S6.setText("6")
        self.cikar = QPushButton(self)
        self.cikar.setText("-")
        #//4. buton//#
        self.S1 = QPushButton(self)
        self.S1.setText("1")
        self.S2 = QPushButton(self)
        self.S2.setText("2")
        self.S3 = QPushButton(self)
        self.S3.setText("3")
        self.topla = QPushButton(self)
        self.topla.setText("+")
        #//5.buton//#
        self.S0 = QPushButton(self)
        self.S0.setText("0")
        self.esit = QPushButton(self)
        self.esit.setText("=")
        
        #//////Ara Layout kapanış/////#
        self.layoutMetin.addWidget(self.metin)
        
        self.layoutClear.addWidget(self.clear)
        self.layoutBol.addWidget(self.bol)
        self.layout2.addLayout(self.layoutClear)
        self.layout2.addLayout(self.layoutBol)
        
        self.layoutS7.addWidget(self.S7)
        self.layoutS8.addWidget(self.S8)
        self.layoutS9.addWidget(self.S9)
        self.layoutCarp.addWidget(self.carp)
        self.layoutRakam1.addLayout(self.layoutS7)
        self.layoutRakam1.addLayout(self.layoutS8)
        self.layoutRakam1.addLayout(self.layoutS9)
        self.layoutRakam1.addLayout(self.layoutCarp)
        
        self.layoutS4.addWidget(self.S4)
        self.layoutS5.addWidget(self.S5)
        self.layoutS6.addWidget(self.S6)
        self.layoutCikar.addWidget(self.cikar)
        self.layoutRakam2.addLayout(self.layoutS4)
        self.layoutRakam2.addLayout(self.layoutS5)
        self.layoutRakam2.addLayout(self.layoutS6)
        self.layoutRakam2.addLayout(self.layoutCikar)
        
        self.layoutS1.addWidget(self.S1)
        self.layoutS2.addWidget(self.S2)
        self.layoutS3.addWidget(self.S3)
        self.layoutTopla.addWidget(self.topla)
        self.layoutRakam3.addLayout(self.layoutS1)
        self.layoutRakam3.addLayout(self.layoutS2)
        self.layoutRakam3.addLayout(self.layoutS3)
        self.layoutRakam3.addLayout(self.layoutTopla)
        
        
        self.layoutS0.addWidget(self.S0)
        self.layoutEsit.addWidget(self.esit)
        self.layoutRakam4.addLayout(self.layoutS0)
        self.layoutRakam4.addLayout(self.layoutEsit)
        
        #/////****ana layout kapanış////#
        self.layoutAna.addLayout(self.layout2)
        self.layoutAna.addLayout(self.layoutRakam1)
        self.layoutAna.addLayout(self.layoutRakam2)
        self.layoutAna.addLayout(self.layoutRakam3)
        self.layoutAna.addLayout(self.layoutRakam4)
        
        
        
        
        
        
        
        
        
        
        
uygulama = QApplication(sys.argv)
pencere = hesap()
pencere.show()
uygulama.exec_()    