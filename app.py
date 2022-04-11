from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'many random bytes'

@app.route('/')
def index():   
    con=sql.connect("dbjual.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("SELECT  * FROM barang")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', barang=data )
 
#fungsi view tambah() untuk membuat form tambah
@app.route('/tambah', methods=['GET','POST'])
def tambah():
   if request.method == 'POST':
      con=sql.connect("dbjual.db")
      cur=con.cursor()
      nama = request.form['nama']
      harga = request.form['harga']
      stok = request.form['stok']
      cur.execute("insert into barang(nama_barang, harga, stok) values (?,?,?)",(nama, harga, stok))
      con.commit()
      flash('Data Barang Berhasil Ditambah...!!!','Success')
      return redirect(url_for('index'))
   else:
      return render_template('tambah.html')
#fungsi view edit() untuk form edit
@app.route('/edit/<id_barang>', methods=['GET','POST'])
def edit(id_barang):
   con=sql.connect("dbjual.db")
   cur=con.cursor()
   cur.execute("select * from barang where id_barang=?",(id_barang,))
   data = cur.fetchone()
   if request.method == 'POST':
      id_barang = request.form['id_barang']
      nama = request.form['nama']
      harga = request.form['harga']
      stok = request.form['stok']
      cur=con.cursor()
      cur.execute("update barang set nama_barang=?,harga=?,stok=? where id_barang=?",(nama,harga,stok,id_barang))
      con.commit()
      flash('Data Barang Berhasil Diupdate...!!!','Success')
      cur.close()
      return redirect(url_for('index'))
   else:
      cur.close()
      return render_template('edit.html', data=data)
#fungsi untuk menghapus data
@app.route('/hapus/<id_barang>', methods=['GET','POST'])
def hapus(id_barang):
   con=sql.connect("dbjual.db")
   cur=con.cursor()
   cur.execute("delete from barang where id_barang=?",(id_barang,))
   con.commit()
   flash('Data Barang Berhasil Didelete...!!!','Warning')
   cur.close()
   return redirect(url_for('index'))
       
if __name__ == '__main__':
   app.run(debug=True)