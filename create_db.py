import sqlite3 as sql

#connect to SQLite
con = sql.connect('dbjual.db')

#Create a Connection
cur = con.cursor()

#Drop barang table if already exsist.
cur.execute("DROP TABLE IF EXISTS barang")

#Create barang table  in dbjual database
sql ='''CREATE TABLE "barang" (
	"id_barang"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"nama_barang"	TEXT,
	"harga"	INTEGER,
    "stok"	INTEGER
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()