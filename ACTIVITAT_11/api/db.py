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

def intents(partida_id: int):
    try:
        conn = db_client()  
        cur = conn.cursor()

        cur.execute(
            "UPDATE partida SET intents = intents + 1 WHERE partida_id = %s",
            (partida_id,)
        )
        conn.commit()

        cur.execute("SELECT intents FROM partida WHERE partida_id = %s", (partida_id,))

        intentos = cur.fetchone()

    finally:
        conn.close()

    return intentos  

def abecedari(idioma: str):
    try:
        conn = db_client()
        cur = conn.cursor()
        
        cur.execute("SELECT Abecedari FROM pantalla WHERE Idioma = %s", (idioma,))
        resultat = cur.fetchone()

        if resultat:
            abecedari = resultat[0]

    finally:
        conn.close()

    return abecedari

def jugador(jugador_id: int):
    try:
        conn = db_client()
        cur = conn.cursor()

        cur.execute("""SELECT Nom, Total_partides, Partides_ganadas, Partides_mes_punts, Punts_partida_actual FROM jugador WHERE ID = %s """, (jugador_id,))
        
        resultat = cur.fetchone()

    finally:
        conn.close()

    return resultat