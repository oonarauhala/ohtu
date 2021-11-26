KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise AssertionError(
                "Kapasiteetin arvo ei ole kokonaisluku tai se on negatiivinen"
            )
        self.kapasiteetti = kapasiteetti
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise AssertionError(
                "Kasvatuskoon arvo ei ole kokonaisluku tai se on negatiivinen"
            )
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_maara = 0

    def kuuluu(self, n):
        if n in self.lukujono:
            return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_maara] = n
            self.alkioiden_maara += 1

            if self.alkioiden_maara == len(self.lukujono):
                self.lukujono.append([0] * self.kasvatuskoko)

    def poista(self, n):
        if self.kuuluu(n):
            self.lukujono.remove(n)
            self.lukujono.append(0)
            self.alkioiden_maara -= 1

    def mahtavuus(self):
        return self.alkioiden_maara

    def to_int_list(self):
        return self.lukujono[: self.alkioiden_maara]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            tulos.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            tulos.lisaa(b_taulu[i])

        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    tulos.lisaa(b_taulu[j])

        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            tulos.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            tulos.poista(b_taulu[i])

        return tulos

    def __str__(self):
        return "{" + ", ".join([str(luku) for luku in self.to_int_list()]) + "}"
