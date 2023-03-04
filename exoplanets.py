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

# from flask import Flask, jsonify

app = Flask(__name__)

# Application routes go here

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
