import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# Define Flask routes to display the data
@app.route('/stars')
def stars():
    # Retrieve data from the stars table
    conn = sqlite3.connect('exoplanets.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM stars")
    rows = cur.fetchall()
    conn.close()

    # Render the stars template with the data
    return render_template('stars.html', rows=rows)




@app.route('/planets')
def planets():
    # Retrieve data from the planets table with star data joined
    conn = sqlite3.connect('exoplanets.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM planets")
    rows = cur.fetchall()
    conn.close()

    # Render the planets template with the data
    return render_template('planets.html', rows=rows)


