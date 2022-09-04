import unittest
import GetAddressIndonesia

class TestScrappingData(unittest.TestCase):
    def test_get_data(self):
        self.assertEqual(
            GetAddressIndonesia.get_data('sragen')[0]['kabupaten'],
            'SRAGEN'
        )
        print("Get Data Success")

    def test_clean_data(self):
        self.assertTrue(
            "SRAGEN" in GetAddressIndonesia.get_by('city')
        )
        print("Clean Data Success")