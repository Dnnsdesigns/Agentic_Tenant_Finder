import sqlite3

def initialize_db():
    conn = sqlite3.connect('tenant_screening.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT,
            budget REAL,
            lease_terms TEXT,
            features TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tenants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            rental_history TEXT,
            credit_score INTEGER,
            employment_status TEXT,
            references TEXT,
            budget REAL,
            features TEXT,
            score REAL
        )
    ''')

    conn.commit()
    conn.close()
