import json
import requests
from colorama import Fore, init
from database import Database

init(autoreset=True)


def get_data(data):
    """
    Get Data From API and Parse Data

    :param data: province / city
    :return: A list of data
    """

    data_fix = []

    API_URL = "https://www.posindonesia.co.id/en/get-address"
    requests_data = requests.get(
        url=API_URL,
        params={
            "term": str(data),
            "_type": "query",
            "q": str(data),
        },
    )
    for _data in requests_data.json()['results']:

        print(Fore.GREEN + "Parsing Data : " + _data['text'] + "")

        # Handle Kelurahan
        if "Kel." in _data['text']:

            kelurahan = _data['text'].split("Kel.")[1].split("Kec.")[0].strip()

            if "KOTA " in _data['text']:
                kecamatan = _data['text'].split("Kec.")[1].split(", KOTA ")[0].strip()

            elif "Kota " in _data['text']:
                kecamatan = _data['text'].split("Kec.")[1].split(", Kota ")[0].strip()

            elif "KAB. " in _data['text']:
                kecamatan = _data['text'].split("Kec.")[1].split(", KAB.")[0].strip()

            elif "Kab. " in _data['text']:
                kecamatan = _data['text'].split("Kec.")[1].split(", Kab.")[0].strip()

            else:
                kecamatan = ""

            if not "KAB." in _data['text']:
                kabupaten = _data['text'].split(", ")[1]
            else:
                kabupaten = _data['text'].split("KAB.")[1].split(",")[0].strip()

            kode_pos = _data['text'].split(",")[2].strip()

            # print("Kelurahan: {}".format(kelurahan))
            # print("Kecamatan: {}".format(kecamatan))
            # print("Kabupaten / Kota : {}".format(kabupaten))
            # print("Kode Pos: {}".format(kode_pos))
            # print("\n")

            data_fix.append({
                "type": "kelurahan",
                "kelurahan": kelurahan,
                "kecamatan": kecamatan,
                "kabupaten": kabupaten,
                "kode_pos": kode_pos,
            })

        # Handle Desa
        elif "Ds." in _data['text']:

            desa = _data['text'].split("Ds.")[1].split("Kec.")[0].strip()

            if "KOTA " in _data['text']:
                kecamatan = _data['text'].split("Kec.")[1].split(", KOTA ")[0].strip()

            elif "Kota " in _data['text']:
                kecamatan = _data['text'].split("Kec.")[1].split(", Kota ")[0].strip()

            else:
                kecamatan = _data['text'].split("Kec.")[1].split(", KAB.")[0].strip()

            if "Kota" in _data['text']:
                kabupaten = _data['text'].split(", ")[1]

            elif "KOTA" in _data['text']:
                kabupaten = _data['text'].split(", ")[1]

            elif "KAB." in _data['text']:
                kabupaten = _data['text'].split("KAB.")[1].split(",")[0].strip()

            elif "Kab." in _data['text']:
                kabupaten = _data['text'].split("Kab.")[1].split(",")[0].strip()
            else:
                kabupaten = ""

            kode_pos = _data['text'].split(",")[2].strip()

            # print("Desa: {}".format(desa))
            # print("Kecamatan: {}".format(kecamatan))
            # print("Kabupaten / Kota : {}".format(kabupaten))
            # print("Kode Pos: {}".format(kode_pos))
            # print("\n")

            data_fix.append({
                "type": "desa",
                "desa": desa,
                "kecamatan": kecamatan,
                "kabupaten": kabupaten,
                "kode_pos": kode_pos,
            })

        # Handle Gp
        elif "Gp." in _data['text']:
            gp = _data['text'].split("Gp.")[1].split("Kec.")[0].strip()

            if "KOTA " in _data['text']:
                kecamatan = _data['text'].split("Kec.")[1].split(", KOTA ")[0].strip()

            elif "Kota " in _data['text']:
                kecamatan = _data['text'].split("Kec.")[1].split(", Kota ")[0].strip()

            else:
                kecamatan = _data['text'].split("Kec.")[1].split(", KAB.")[0].strip()

            if "Kota" in _data['text']:
                kabupaten = _data['text'].split(", ")[1]

            elif "KOTA" in _data['text']:
                kabupaten = _data['text'].split(", ")[1]

            else:
                kabupaten = _data['text'].split("KAB.")[1].split(",")[0].strip()

            kode_pos = _data['text'].split(",")[2].strip()

            # print("Gp: {}".format(gp))
            # print("Kecamatan: {}".format(kecamatan))
            # print("Kabupaten / Kota : {}".format(kabupaten))
            # print("Kode Pos: {}".format(kode_pos))
            # print("\n")

            data_fix.append({
                "type": "gp",
                "desa": gp,
                "kecamatan": kecamatan,
                "kabupaten": kabupaten,
                "kode_pos": kode_pos,
            })

        # Handle Nag
        elif "Nag." in _data['text']:
            nag = _data['text'].split("Nag.")[1].split("Kec.")[0].strip()

            if "KOTA " in _data['text']:
                kecamatan = _data['text'].split("Kec.")[1].split(", KOTA ")[0].strip()

            elif "Kota " in _data['text']:
                kecamatan = _data['text'].split("Kec.")[1].split(", Kota ")[0].strip()

            else:
                kecamatan = _data['text'].split("Kec.")[1].split(", KAB.")[0].strip()

            if "Kota" in _data['text']:
                kabupaten = _data['text'].split(", ")[1]

            elif "KOTA" in _data['text']:
                kabupaten = _data['text'].split(", ")[1]

            else:
                kabupaten = _data['text'].split("KAB.")[1].split(",")[0].strip()

            kode_pos = _data['text'].split(",")[2].strip()

            # print("Nag: {}".format(nag))
            # print("Kecamatan: {}".format(kecamatan))
            # print("Kabupaten / Kota : {}".format(kabupaten))
            # print("Kode Pos: {}".format(kode_pos))
            # print("\n")

            data_fix.append({
                "type": "nag",
                "desa": nag,
                "kecamatan": kecamatan,
                "kabupaten": kabupaten,
                "kode_pos": kode_pos,
            })
    return data_fix


def get_by(a="province"):
    """
    Get Data From data_list.json and clean duplicate data

    :param a: province / city
    :return: A list clean data
    """

    # Get Data From data_list.json
    with open('data_list.json', 'r') as f:
        data_list = f.read()

    # Select data by province / city
    data_unclean = []
    for _listdata in json.loads(data_list)['data']:
        data_unclean.append(_listdata[a])

    # Clean Data
    data_clean = list(set(data_unclean))
    return data_clean


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
