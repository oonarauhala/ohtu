from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        pass
        self.ostokset_lista = []

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in self.ostokset_lista)

    def hinta(self):
        return sum(ostos.hinta() for ostos in self.ostokset_lista)

    def lisaa_tuote(self, lisattava: Tuote):
        tuote_listassa = False
        for ostos in self.ostokset_lista:
            if lisattava.nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(1)
                tuote_listassa = True
                break
        if not tuote_listassa:
            self.ostokset_lista.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        tuote_listassa = False
        for ostos in self.ostokset_lista:
            if poistettava.nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(-1)
                tuote_listassa = True
                break

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostokset_lista
