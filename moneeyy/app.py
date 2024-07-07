from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'manga.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS manga (
                id INTEGER PRIMARY KEY,
                manganame TEXT NOT NULL,
                artist TEXT NOT NULL,
                pages INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def store():
    manganame = request.form['manganame']
    artist = request.form['artist']
    pages = request.form['pages']
    price = request.form['price']

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO manga (manganame, artist, pages, price) VALUES (?, ?, ?, ?)',
                       (manganame, artist, pages, price))
        conn.commit()

    return redirect(url_for('index'))

@app.route('/info')
def show_info():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM manga')
        manga_list = cursor.fetchall()
    return render_template('manga_info.html', manga_list=manga_list)

@app.route('/all')
def display_all():
    artist = request.args.get('artist')
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM manga WHERE artist = ?', (artist,))
        manga_list = cursor.fetchall()
    return render_template('all_manga.html', manga_list=manga_list)

@app.route('/titles')
def list_titles():
    manganame = request.args.get('manganame')
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM manga WHERE manganame = ?', (manganame,))
        manga_list = cursor.fetchall()
    return render_template('manga_titles.html', manga_list=manga_list)

@app.route('/count')
def count_manga():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM manga')
        count = cursor.fetchone()[0]
    return f'<h1>No of manga in library: {count}</h1>'

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
