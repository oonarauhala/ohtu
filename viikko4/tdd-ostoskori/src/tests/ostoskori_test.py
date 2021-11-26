import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        # self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yksi_tuote_ostoskorin_hinta_sama_kuin_tuotteen_hinta(self):
        leipa = Tuote("Leipa", 2)
        self.kori.lisaa_tuote(leipa)
        self.assertEqual(self.kori.hinta(), leipa.hinta())

    def test_kahden_tuotteen_lisayksen_jalkeen_korissa_2_tuotetta(self):
        leipa = Tuote("Leipa", 2)
        porkkana = Tuote("Porkkana", 1)
        self.kori.lisaa_tuote(leipa)
        self.kori.lisaa_tuote(porkkana)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisayksenjalkeen_korin_hinta_sama_kuin_kahden_tuotteen_summa(
        self,
    ):
        leipa = Tuote("Leipa", 2)
        porkkana = Tuote("Porkkana", 1)
        self.kori.lisaa_tuote(leipa)
        self.kori.lisaa_tuote(porkkana)
        self.assertEqual(self.kori.hinta(), 3)
