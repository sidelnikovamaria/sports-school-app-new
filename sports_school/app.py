from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'sports-school-2024')

def init_db():
    conn = sqlite3.connect('sports_school.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS coaches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        birth_date DATE NOT NULL,
        gender TEXT NOT NULL,
        sport_type TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS athletes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        birth_date DATE NOT NULL,
        gender TEXT NOT NULL,
        sport_type TEXT NOT NULL,
        coach_id INTEGER
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS schedule (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        coach_id INTEGER NOT NULL,
        day_of_week TEXT NOT NULL,
        start_time TIME NOT NULL,
        end_time TIME NOT NULL,
        activity_type TEXT NOT NULL,
        location TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Спортивная школа</title>
        <style>
            body { font-family: Arial; margin: 40px; }
            h1 { color: #2c3e50; }
            .menu { margin: 20px 0; }
            .menu a { 
                display: inline-block; 
                margin: 10px; 
                padding: 10px 20px; 
                background: #3498db; 
                color: white; 
                text-decoration: none;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <h1>🏃 Спортивная школа</h1>
        <p>Система управления тренерами и спортсменами</p>
        
        <div class="menu">
            <a href="/coaches">👨‍🏫 Тренеры</a>
            <a href="/athletes">🏃 Спортсмены</a>
            <a href="/schedule">📅 Расписание</a>
            <a href="/assignments">👥 Назначения</a>
        </div>
    </body>
    </html>
    '''

@app.route('/coaches')
def coaches():
    return '<h1>Тренеры</h1><p>Страница тренеров работает!</p><a href="/">На главную</a>'

@app.route('/athletes')
def athletes():
    return '<h1>Спортсмены</h1><p>Страница спортсменов работает!</p><a href="/">На главную</a>'

@app.route('/schedule')
def schedule():
    return '<h1>Расписание</h1><p>Страница расписания работает!</p><a href="/">На главную</a>'

@app.route('/assignments')
def assignments():
    return '<h1>Назначения</h1><p>Страница назначений работает!</p><a href="/">На главную</a>'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    flash('Тренировка удалена из расписания!', 'success')
    return redirect(url_for('schedule'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
