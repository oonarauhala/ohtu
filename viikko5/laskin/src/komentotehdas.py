class Komentotehdas:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka
        self.komennot = {
            1: Summa(sovelluslogiikka),
            2: Miinus(sovelluslogiikka),
            3: Nollaus(sovelluslogiikka),
        }

    def hae(self, komento):
        if komento in self.komennot:
            return self.komennot[komento]
        return None


class Summa:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self, arvo):
        self.sovelluslogiikka.plus(arvo)


class Miinus:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self, arvo):
        self.sovelluslogiikka.miinus(arvo)


class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self, arvo):
        self.sovelluslogiikka.nollaa()
