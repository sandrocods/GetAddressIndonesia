import json
from colorama import Fore, init
from database import Database
from GetAddressIndonesia import get_data, get_by

init(autoreset=True)




database = Database('data.db')


#
# database.reset_database()
#

# Insert to Database
for _listdata in get_by('city'):
    print(Fore.RED + "Parsing Data : " + _listdata + "")
    for i in get_data(_listdata):

        json_decode = json.loads(json.dumps(i))
        print(Fore.LIGHTYELLOW_EX + "Inserting Data : " + str(json_decode) + "")

        if json_decode['type'] == "desa":

            database.insert_data(
                desa=json_decode['desa'],
                kecamatan=json_decode['kecamatan'],
                kabupaten_kota=json_decode['kabupaten'],
                kode_pos=json_decode['kode_pos'],
                kelurahan=None,
            )

        elif json_decode['type'] == "gp":

            database.insert_data(
                kelurahan=None,
                desa=json_decode['desa'],
                kecamatan=json_decode['kecamatan'],
                kabupaten_kota=json_decode['kabupaten'],
                kode_pos=json_decode['kode_pos'],
            )

        elif json_decode['type'] == "nag":

            database.insert_data(
                kelurahan=None,
                desa=json_decode['desa'],
                kecamatan=json_decode['kecamatan'],
                kabupaten_kota=json_decode['kabupaten'],
                kode_pos=json_decode['kode_pos'],
            )

        elif json_decode['type'] == "kelurahan":

            database.insert_data(
                desa=None,
                kelurahan=json_decode['kelurahan'],
                kecamatan=json_decode['kecamatan'],
                kabupaten_kota=json_decode['kabupaten'],
                kode_pos=json_decode['kode_pos'],
            )
