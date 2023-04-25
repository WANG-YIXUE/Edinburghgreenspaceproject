from flask import Flask, Blueprint, render_template
import cx_Oracle
import cgi
import cgitb
import os
cgitb.enable()

data = Blueprint('data', __name__)

@data.route('/data')
def database():
    with open("../../nada",'r') as pwf:
          pw = pwf.read().strip()
    conn = cx_Oracle.connect(dsn="geoslearn", user="s2236682", password=pw)
    c = conn.cursor()
    c.execute("SELECT * FROM GREENSPACE")
    col = c.fetchone() [0]
    conn.close()
    return render_template('data.html', database='c')
#    return '<h1>Data</h1>'


#def data():
#    with open("../../../nada",'r') as pwf:
#          pw = pwf.read().strip()
#    conn = cx_Oracle.connect(dsn="geoslearn", user="s2236682", password=pw)
#    c = conn.cursor()
#    c.execute("SELECT * FROM GREENSPACE")
#    col = c.fetchone() [0]
#    conn.close()
#    return render_template('data.html')
