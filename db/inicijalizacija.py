import sqlite3
def incijalizuj_bazu(db_path:str='banka.db')->None:

    with sqlite3.connect(db_path) as conn:
        conn.executescript(""""" """)