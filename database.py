import sqlalchemy
from sqlalchemy import Column, Integer, String, MetaData
import json


class Database:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlalchemy.create_engine('sqlite:///' + self.db_name)
        self.table = sqlalchemy.Table('data', MetaData(), autoload=True, autoload_with=self.conn)

    def create_table(self):
        metadata = MetaData()
        self.table = sqlalchemy.Table(
            'data', metadata,
            Column('id', Integer, primary_key=True),
            Column('desa', String),
            Column('kecamatan', String),
            Column('kelurahan', String),
            Column('kabupaten_kota', String),
            Column('kode_pos', String)
        )
        metadata.create_all(self.conn)

    def insert_data(self, desa, kecamatan, kelurahan, kabupaten_kota, kode_pos):
        conn = self.conn.connect()
        insert = self.table.insert().values(
            desa=desa,
            kecamatan=kecamatan,
            kelurahan=kelurahan,
            kabupaten_kota=kabupaten_kota,
            kode_pos=kode_pos
        )
        conn.execute(insert)

    def reset_database(self):
        try:
            self.table.drop(self.conn)
            self.create_table()
        except Exception as e:
            self.create_table()

    def search_multi(self, search):

        conn = self.conn.connect()
        query = sqlalchemy.select([self.table]).where(
            self.table.c.desa.like('%' + search + '%') |
            self.table.c.kelurahan.like('%' + search + '%') |
            self.table.c.kecamatan.like('%' + search + '%') |
            self.table.c.kabupaten_kota.like('%' + search + '%') |
            self.table.c.kode_pos.like('%' + search + '%')
        )
        # https://stackoverflow.com/questions/52449901/typeerror-object-of-type-resultproxy-is-not-json-serializable-result-in-sqlalc
        self.data = [dict(row) for row in conn.execute(query)]
        return json.dumps(self.data, indent=4)