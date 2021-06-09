


def vnesi_crko(prompt):
    x = input(prompt)
    while True:
        if len(x) == 1 and x.isalpha():
            return x.lower()
        else:
            if len(x) > 1 or len(x) == 0:
                print('Vnesli ste preveč ali premalo črk, število črk mora biti enako 1.')
            if not x.isalpha():
                print('Vnesti morate črko')
            x = input(prompt)


def pokazi_besedo(beseda, mnozica):
    prikaz = ''
    for i, crka in enumerate(beseda):
        if crka in mnozica:
            prikaz += crka
        else:
            prikaz += '_'
    print(prikaz)

beseda = input('Vnesi besedo, ki jo bo oseba iskala: ')
n = 0
ugibane_crke = set()
uganjene_crke = set()
#joze = Hangman()
#animacija_obesenca = {1: joze.spodnji_temelj(), 2: joze.konstrukcija_z_vrvjo(),
                      #3: joze.glava_vrat(), 4: joze.roki(), 5: joze.trupek(), 6: joze.noga_d(),
                      #7: joze.noga_l()}

while True:
    pokazi_besedo(beseda, ugibane_crke)

    crka = vnesi_crko('Ugibaj črko: ')

    if crka in ugibane_crke:
        print('S to črko si že poizkusil/a!')
        crka = vnesi_crko('Ugibaj ponovno: ')
    ugibane_crke.add(crka)

    if not crka in beseda:
        n += 1

    else:
        uganjene_crke.add(crka)

    if n == 7:
        pokazi_besedo(beseda, ugibane_crke)
        print('Konec igre. 7x si zgrešil črke.')

        import risar
        import math


        def trikotnik():
            risar.crta(150, 400, 180, 430)
            risar.crta(150, 400, 120, 430)
            risar.crta(180, 430, 120, 430)


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
        break

    if len(uganjene_crke) == len(set(beseda)):
        print(f'Bravo, uganil si besedo! Iskana beseda je {beseda}')
        break












