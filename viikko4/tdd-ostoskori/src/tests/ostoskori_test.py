import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.leipa = Tuote("Leipa", 2)
        self.porkkana = Tuote("Porkkana", 1)
        self.maito = Tuote("Maito", 3)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yksi_tuote_ostoskorin_hinta_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.leipa)
        self.assertEqual(self.kori.hinta(), self.leipa.hinta())

    def test_kahden_tuotteen_lisayksen_jalkeen_korissa_2_tuotetta(self):
        self.kori.lisaa_tuote(self.leipa)
        self.kori.lisaa_tuote(self.porkkana)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisayksenjalkeen_korin_hinta_sama_kuin_kahden_tuotteen_summa(
        self,
    ):
        self.kori.lisaa_tuote(self.leipa)
        self.kori.lisaa_tuote(self.porkkana)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_saman_tuotteen_lisayksen_jalkeen_korissa_2_tuotetta(self):
        self.kori.lisaa_tuote(self.leipa)
        self.kori.lisaa_tuote(self.leipa)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_2_saman_tuotteen_lisayksen_jalkeen_korin_hinta_sama_kuin_tuotteiden_summa(
        self,
    ):
        self.kori.lisaa_tuote(self.leipa)
        self.kori.lisaa_tuote(self.leipa)
        self.assertEqual(self.kori.hinta(), 4)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(
        self,
    ):
        self.kori.lisaa_tuote(self.maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_2_eri_tuotteen_lisayksen_jalkeen_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.porkkana)
        self.kori.lisaa_tuote(self.leipa)
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_2_saman_tuotteen_lisäys_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.porkkana)
        self.kori.lisaa_tuote(self.porkkana)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_2_saman_tuotteen_lisayksen_jalkeen_korissa_ostos_sama_nimi_kuin_tuotteella_lukumaara_2(
        self,
    ):
        self.kori.lisaa_tuote(self.porkkana)
        self.kori.lisaa_tuote(self.porkkana)
        self.assertEqual(self.kori.ostokset()[0].tuotteen_nimi(), "Porkkana")
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 2)

    def test_poista_ostoksesta_yksi_tuote(self):
        self.kori.lisaa_tuote(self.porkkana)
        self.kori.lisaa_tuote(self.porkkana)
        self.kori.poista_tuote(self.porkkana)
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 1)
