class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = 0

    def miinus(self, arvo):
        self.aseta_edellinen()
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.aseta_edellinen()
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.aseta_edellinen()
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.aseta_edellinen()
        self.tulos = arvo

    def aseta_edellinen(self):
        self.edellinen = self.tulos
