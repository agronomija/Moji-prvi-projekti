from PyQt5 import QtWidgets, uic
import psycopg2

#from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
import collections


slovar_gesel = collections.defaultdict(list)   #sem se bodo shranjevala gesla, email,
imena_aplikacij = ''

app = QApplication([])
dlg = uic.loadUi('gesla2020.ui')


def shrani():
    #ikone v designerju
    ime_app = dlg.leImeappa.text()
    uporabnisko_ime = dlg.leUsername.text()
    email = dlg.leEmail.text()
    geslo = dlg.leGeslo.text()

    with open('gesla.csv', 'a', encoding='utf-8') as datoteka:
        datoteka.write(f'{ime_app},{uporabnisko_ime},{email},{geslo}\n')
    #slovar_gesel[ime_app] = [uporabnisko_ime, email, geslo]
    #nastavijo zgornje ikkone nazaj na prazno
    dlg.leImeappa.setText('')
    dlg.leUsername.setText('')
    dlg.leEmail.setText('')
    dlg.leGeslo.setText('')

    #if ime_app != '':
     #   dlg.label_5.setText(f'{dlg.label_5.text()}\n {ime_app}')

    if ime_app != '':
        dlg.label_5.setText(f'{dlg.label_5.text()}\n {ime_app}')


def povej_podatke():
    ime_appa2 = dlg.leImeappa2.text()


    if ime_appa2 in slovar_gesel:

        up_ime, mejl, passw = slovar_gesel[ime_appa2]
        dlg.lbVrnjeniPodatki.setText(
            f'Ime aplikacije: {ime_appa2}\nUporabniško ime: {up_ime}\nEmail: {mejl},\nGeslo: {passw}')

    elif not ime_appa2 in slovar_gesel:
        dlg.lbVrnjeniPodatki.setText(
            f'Pod {ime_appa2} ni\n shranjene nobene aplikacije.')




def povej_podatke_proba():
    ime_appa2 = dlg.leImeappa2.text()

    with open('gesla.csv', 'r', encoding='utf-8') as datoteka:
        for vrstica in datoteka.read().splitlines():
            if vrstica and ime_appa2 == vrstica.split(',')[0]:
                ime_appa2, up_ime, mejl, passw = vrstica.split(',')
                dlg.lbVrnjeniPodatki.setText(
                    f'Ime aplikacije: {ime_appa2}\nUporabniško ime: {up_ime}\nEmail: {mejl},\nGeslo: {passw}')
                break
            elif not ime_appa2 in slovar_gesel:
                dlg.lbVrnjeniPodatki.setText(
                    f'Pod {ime_appa2} ni\n shranjene nobene aplikacije.')

    #if ime_appa2 in slovar_gesel:

     #   up_ime, mejl, passw = slovar_gesel[ime_appa2]
      #  dlg.lbVrnjeniPodatki.setText(
       #     f'Ime aplikacije: {ime_appa2}\nUporabniško ime: {up_ime}\nEmail: {mejl},\nGeslo: {passw}')

    #elif not ime_appa2 in slovar_gesel:
     #   dlg.lbVrnjeniPodatki.setText(
      #      f'Pod {ime_appa2} ni\n shranjene nobene aplikacije.')





dlg.btSave.clicked.connect(shrani)
dlg.btVrnigesla.clicked.connect(povej_podatke_proba)

dlg.show()
app.exec()

