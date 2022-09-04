from database import Database

database = Database('data.db')

print("==" * 20 + " Search by kode pos " + "==" * 20)
# Search by kode pos
print(
    database.search_multi('57211')

)

print("==" * 20 + " Search by kelurahan " + "==" * 20)
# search by kelurahan
print(
    database.search_multi('Sragen Tengah')

)

print("==" * 20 + " Search by kecamatan " + "==" * 20)
# search by kecamatan
print(
    database.search_multi('Sragen')
)

print("==" * 20 + " Search by kabupaten " + "==" * 20)
# search by kabupaten
print(
    database.search_multi('Sragen')
)

print("==" * 20 + " Search by desa " + "==" * 20)
# search by desa
print(
    database.search_multi('Pilangsari')
)

print("==" * 20 + " Clean Data " + "==" * 20)

from GetAddressIndonesia import get_by

for i in get_by('city'):
    print(i)