import unittest
from database import Database
import json


class TestDatabase(unittest.TestCase):

    # test kode pos
    def test_search_multi(self):
        database = Database('../data.db')
        self.assertEqual(
            json.loads(database.search_multi('57211'))[0]['kode_pos'],
            '57211'
        )
        print("Search Multi by kode pos Success")

    # test kelurahan
    def test_search_multi_1(self):
        database = Database('../data.db')
        self.assertEqual(
            json.loads(database.search_multi('Sragen Tengah'))[0]['kelurahan'],
            'Sragen Tengah'
        )
        print("Search Multi by kelurahan Success")

    # test kecamatan
    def test_search_multi_2(self):
        database = Database('../data.db')
        self.assertEqual(
            json.loads(database.search_multi('Sragen'))[0]['kecamatan'],
            'Sragen'
        )
        print("Search Multi by kecamatan Success")

    # test kabupaten
    def test_search_multi_3(self):
        database = Database('../data.db')
        self.assertEqual(
            json.loads(database.search_multi('Sragen'))[0]['kabupaten_kota'],
            'SRAGEN'
        )
        print("Search Multi by kabupaten Success")

    # test desa
    def test_search_multi_4(self):
        database = Database('../data.db')
        self.assertEqual(
            json.loads(database.search_multi('Pilangsari'))[0]['desa'],
            'Pilangsari'
        )
        print("Search Multi by desa Success")
