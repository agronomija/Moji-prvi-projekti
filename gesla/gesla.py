from PyQt5 import QtWidgets, uic

#from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
import collections


class gesla():
    def __init__(self):
        self.podatki = collections.defaultdict(list)

    def dodaj_podatke(self, ime_app, uporabnisko_ime, email, geslo):
        #ime_app = dlg.leImeappa.text()
        #uporabnisko_ime = dlg.leUsername.text()
        #email = dlg.leEmail.text()
        #geslo = dlg.leGeslo.text()
        self.podatki[ime_app] = [uporabnisko_ime, email, geslo]

    def vrni_podatke(self, ime_app):

        if ime_app in self.podatki:
            up_ime = self.podatki[ime_app][0]
            email = self.podatki[ime_app][1]
            geslo = self.podatki[ime_app][2]
            dlg.lbVrnjeniPodatki.setText(f'Za {ime_app}:\nUporabniško ime: {up_ime}\nEmail: {email}\nGeslo: {geslo}')
        else:
            dlg.lbVrnjeniPodatki.setText(f'Pod tem imenom ni shranjenega ničesar.')



app = QApplication([])
dlg = uic.loadUi('gesla2020.ui')

vasa_gesla = gesla()

ime_app = dlg.leImeappa.text()
uporabnisko_ime = dlg.leUsername.text()
email = dlg.leEmail.text()
geslo = dlg.leGeslo.text()


dlg.btSave.clicked.connect(vasa_gesla.dodaj_podatke(ime_app, uporabnisko_ime, email, geslo ))
dlg.btVrnigesla.clicked.connect(vasa_gesla.vrni_podatke(dlg.leImeappa2.text()))

dlg.show()
app.exec()