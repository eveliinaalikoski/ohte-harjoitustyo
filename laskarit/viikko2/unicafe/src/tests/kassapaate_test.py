import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaatteen_rahamaara_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_edullisten_lounaiden_maara_oikein_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myytyjen_maukkaiden_lounaiden_maara_oikein_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassa_rahat_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)

    # EDULLINEN LOUNAS
    # rahat riittää
    def test_maksu_riittava_kassan_rahamaara_kasvaa_edullinen_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maksu_riittava_oikea_vaihtoraha_edullinen_kateinen(self):
        testi=self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(testi, 260)

    def test_maksu_riittava_lounaiden_maara_kasvaa_edullinen_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maksu_riittava_veloitetaan_oikein_kortilta_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_maksu_riittava_palautetaan_true(self):
        testi=self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(testi, True)

    def test_maksu_riittava_lounaiden_maara_kasvaa_edullinen_kortti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    # rahat ei riitä
    def test_maksu_ei_riittava_kassan_rahamaara_ei_muutu_edullinen_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maksu_ei_riittava_oikea_vaihtoraha_edullinen_kateinen(self):
        testi=self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(testi, 100)

    def test_maksu_ei_riittava_lounaiden_maara_ei_kasva_edullinen_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maksu_ei_riittava_kortin_rahamaara_ei_muutu_edullinen(self):
        kortti=Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)

    def test_maksu_ei_riittava_edullisesti_palautetaan_false(self):
        kortti=Maksukortti(200)
        testi=self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(testi, False)

    def test_maksu_ei_riittava_lounaiden_maara_ei_kasva_edullinen_kortti(self):
        kortti=Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    # MAUKAS LOUNAS
    # rahat riittää
    def test_maksu_riittava_kassan_rahamaara_kasvaa_maukas_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maksu_riittava_oikea_vaihtoraha_maukas_kateinen(self):
        testi=self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(testi, 100)

    def test_maksu_riittava_lounaiden_maara_kasvaa_maukas_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maksu_riittava_veloitetaan_oikein_kortilta_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_maksu_riittava_palautetaan_true(self):
        testi=self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(testi, True)

    def test_maksu_riittava_lounaiden_maara_kasvaa_maukas_kortti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    # rahat ei riitä
    def test_maksu_ei_riittava_kassan_rahamaara_ei_muutu_maukas_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maksu_ei_riittava_oikea_vaihtoraha_maukas_kateinen(self):
        testi=self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(testi, 100)

    def test_maksu_ei_riittava_lounaiden_maara_ei_kasva_maukas_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maksu_ei_riittava_kortin_rahamaara_ei_muutu_maukas(self):
        kortti=Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)

    def test_maksu_ei_riittava_maukkaasti_palautetaan_false(self):
        kortti=Maksukortti(200)
        testi=self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(testi, False)

    def test_maksu_ei_riittava_lounaiden_maara_ei_kasva_maukas_kortti(self):
        kortti=Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # RAHA EI MUUTU KORTTIOSTO
    def test_kassassa_oleva_rahamaara_ei_muutu_kortti_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_oleva_rahamaara_ei_muutu_kortti_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # RAHAN LATAUS
    def test_rahaa_ladattaessa_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_rahaa_ladattaessa_kassan_rahamaara_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_negatiivisen_summan_lataus_ei_muuta_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.maksukortti.saldo, 1000)
