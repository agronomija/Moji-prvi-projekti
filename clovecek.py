

import risar
import math

def trikotnik():
    risar.crta(150,400, 180, 430)
    risar.crta(150,400, 120, 430)
    risar.crta(180,430,120,430)

class Hangman:
    def __init__(self):
        pass
        self.temelj = trikotnik()
        self.glavna_steber = risar.crta(150, 20, 150, 400)
        self.gornja_letev = risar.crta(300, 20, 150, 20)
        self.strik = risar.crta(300, 70, 300, 20)
        self.glava = risar.krog(300, 100, 30)
        self.vrat = risar.crta(300, 130, 300, 150)
        self.d_roka_dol = risar.crta(300, 150, 350, 170)
        self.l_roka_dol = risar.crta(300, 150, 250, 170)
        self.d_roka_gor = risar.crta(300, 150, 350, 130)
        self.l_roka_gor = risar.crta(300, 150, 250, 130)
        self.trup = risar.crta(300, 150, 300, 220)
        self.d_noga_dol = risar.crta(300, 220, 350, 300)
        self.l_noga_dol = risar.crta(300, 220, 250, 300)

    def roki_dol(self):

        self.d_roka_gor.show()
        self.l_roka_gor.show()
        self.d_roka_dol.hide()
        self.l_roka_dol.hide()

    def roki_gor(self):

        self.d_roka_gor.hide()
        self.l_roka_gor.hide()
        self.d_roka_dol.show()
        self.l_roka_dol.show()

    def spodnji_temelj(self):
        self.temelj = trikotnik()

    def konstrukcija_z_vrvjo(self):
        self.glavna_steber = risar.crta(150, 20, 150, 400)
        self.gornja_letev = risar.crta(300, 20, 150, 20)
        self.strik = risar.crta(300, 70, 300, 20)

    def glava_vrat(self):
        self.glava = risar.krog(300, 100, 30)
        self.vrat = risar.crta(300, 130, 300, 150)

    def roki(self):
        self.d_roka_dol = risar.crta(300, 150, 350, 170)
        self.l_roka_dol = risar.crta(300, 150, 250, 170)

    def trupek(self):
        self.trup = risar.crta(300, 150, 300, 220)

    def noga_d(self):
        self.d_noga_dol = risar.crta(300, 220, 350, 300)

    def noga_l(self):
        self.l_noga_dol = risar.crta(300, 220, 250, 300)






joze = Hangman()
for i in range(100):
    joze.roki_gor()
    risar.cakaj(0.1)
    joze.roki_dol()
    risar.cakaj(0.1)

risar.stoj()


#def obesen():
  #  joze = Clovecek()
  #  for i in range(100):
   #     joze.roki_gor()
    #    risar.cakaj(0.1)
     #   joze.roki_dol()
      #  risar.cakaj(0.1)

    #risar.stoj()






