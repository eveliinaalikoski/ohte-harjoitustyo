import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_saldo_vahenee_oikein_jos_on_rahaa(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")

    def test_saldo_muuttuu_jos_ei_tarpeeksi_rahaa(self):
        testi=self.maksukortti.ota_rahaa(2000)
        self.assertEqual(testi, False)

    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        testi=self.maksukortti.ota_rahaa(2000)
        self.assertEqual(testi, False)
