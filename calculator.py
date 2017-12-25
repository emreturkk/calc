import sys
from PyQt5 import  QtWidgets


class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Hesap Makinası")


        self.init_ui()


    def init_ui(self):

        self.yazı_alanı = QtWidgets.QLineEdit()
        self.yazı_alanı2 = QtWidgets.QLineEdit()
        self.sonuc = QtWidgets.QLabel("sonuç için birinci ve ikinci kutuyu doldurunuz")
        self.toplama = QtWidgets.QPushButton("topla")
        self.cıkarma = QtWidgets.QPushButton("çıkar")
        self.carpma = QtWidgets.QPushButton("çarp")
        self.bölme = QtWidgets.QPushButton("böl")
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdır = QtWidgets.QPushButton("Yazdır")


        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.yazı_alanı2)
        v_box.addWidget(self.sonuc)
        v_box.addWidget(self.toplama)
        v_box.addWidget(self.cıkarma)
        v_box.addWidget(self.carpma)
        v_box.addWidget(self.bölme)
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdır)
        v_box.addStretch()

        self.setLayout(v_box)


        self.toplama.clicked.connect(self.click)
        self.cıkarma.clicked.connect(self.click)
        self.carpma.clicked.connect(self.click)
        self.bölme.clicked.connect(self.click)
        self.temizle.clicked.connect(self.click)
        self.yazdır.clicked.connect(self.click)



        self.show()

    def click(self):
        sender = self.sender()

        if sender.text() ==  "topla":
            self.sonuc.setText("sonuc = {}".format(int(self.yazı_alanı.text())+int(self.yazı_alanı2.text())))
        elif sender.text()=="çıkar":
            self.sonuc.setText("sonuc = {}".format(int(self.yazı_alanı.text()) - int(self.yazı_alanı2.text())) )
        elif sender.text() == "çarp":
            self.sonuc.setText("sonuc = {}".format(int(self.yazı_alanı.text()) * int(self.yazı_alanı2.text())) )
        elif sender.text() == "böl":
            self.sonuc.setText("sonuc = {}".format(int(self.yazı_alanı.text()) / int(self.yazı_alanı2.text())) )
        elif sender.text() == "Temizle":
            self.yazı_alanı.clear()
            self.yazı_alanı2.clear()

        else:
            print("girdiğiniz {} , {} değerlerinde sorun vardır".format(self.yazı_alanı.text(),self.yazı_alanı2.text()))



app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())