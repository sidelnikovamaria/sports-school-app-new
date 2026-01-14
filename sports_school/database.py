import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('sports_school.db')
    cursor = conn.cursor()
    
    # Создание таблицы тренеров
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS coaches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        birth_date DATE NOT NULL,
        gender TEXT NOT NULL,
        sport_type TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Создание таблицы спортсменов
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS athletes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        birth_date DATE NOT NULL,
        gender TEXT NOT NULL,
        sport_type TEXT NOT NULL,
        coach_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (coach_id) REFERENCES coaches (id)
    )
    ''')
    
    # Создание таблицы расписания
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS schedule (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        coach_id INTEGER NOT NULL,
        day_of_week TEXT NOT NULL,
        start_time TIME NOT NULL,
        end_time TIME NOT NULL,
        activity_type TEXT NOT NULL,
        location TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (coach_id) REFERENCES coaches (id)
    )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('sports_school.db')
    conn.row_factory = sqlite3.Row
    return conn
