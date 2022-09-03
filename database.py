import sqlalchemy
from sqlalchemy import Column, Integer, String, MetaData


class Database:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlalchemy.create_engine('sqlite:///' + self.db_name)
        self.table = sqlalchemy.Table('data', sqlalchemy.MetaData())

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
