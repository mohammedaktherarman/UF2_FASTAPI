import mysql.connector
from connection import db_client

def pillafrase(Idioma: str):
    try:
        conn = db_client()
        cur = conn.cursor()

        cur.execute("SELECT frase FROM pantalla WHERE Idioma = %s", (Idioma,))
        frase = cur.fetchall()

    finally:
        conn.close()
    return frase
