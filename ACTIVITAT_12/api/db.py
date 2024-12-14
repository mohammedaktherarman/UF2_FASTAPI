import mysql.connector
from connection import db_client

# CRUD TAULA JUGADOR 
def get_jugador(jugador_id: int):
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM jugador WHERE ID = %s", (jugador_id,))
        resultado = cur.fetchone()
    finally:
        conn.close()
    return resultado

def create_jugador(Nom: str, Total_partides: int, Partides_ganadas: int, Partides_amb_mes_punts: int, Punts_partida_actual: int):
    try:
        conn = db_client()
        cur = conn.cursor()
        sql = """INSERT INTO jugador (Nom, Total_partides, Partides_ganadas, Partides_amb_mes_punts, Punts_partida_actual) VALUES (%s, %s, %s, %s, %s)"""
        values = (Nom, Total_partides, Partides_ganadas, Partides_amb_mes_punts, Punts_partida_actual)
        cur.execute(sql, values)
        conn.commit()
    finally:
        conn.close()

def update_jugador(jugador_id: int, Nom: str, Total_partides: int, Partides_ganades: int, Partides_amb_mes_punts: int, Punts_partida_actual: int):
    try:
        conn = db_client()
        cur = conn.cursor()

        cur.execute("""UPDATE jugador SET Nom = %s, Total_partides = %s, Partides_ganades = %s, Partides_amb_mes_punts = %s, Punts_partida_actual = %s WHERE ID = %s""", (Nom, Total_partides, Partides_ganades, Partides_amb_mes_punts, Punts_partida_actual, jugador_id))
        conn.commit()
    finally:
        conn.close()

def delete_jugador(jugador_id: int):
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("DELETE FROM jugador WHERE ID = %s", (jugador_id,))
        conn.commit()
    finally:
        conn.close()

# CRUD TAULA PARAULES
def get_paraula(paraula: str):
    try:
        conn = db_client()
        cur = conn.cursor()

        cur.execute("SELECT * FROM paraules WHERE paraula = %s", (paraula,))
        resultado = cur.fetchone()
    finally:
        conn.close()
    return resultado

def create_paraula(paraula: str, theme: str):
    try:
        conn = db_client()
        cur = conn.cursor()

        sql = "INSERT INTO paraules (paraula, theme) VALUES (%s, %s)"
        values = (paraula, theme)
        cur.execute(sql, values)
        conn.commit()
    finally:
        conn.close()

def update_paraula(paraula: str, theme: str):
    try:
        conn = db_client()
        cur = conn.cursor()

        cur.execute("UPDATE paraules SET theme = %s WHERE paraula = %s", (theme, paraula))
        conn.commit()
    finally:
        conn.close()

def delete_paraula(paraula: str):
    try:
        conn = db_client()
        cur = conn.cursor()

        cur.execute("DELETE FROM paraules WHERE paraula = %s", (paraula,))
        conn.commit()
    finally:
        conn.close()

# CRUD TAULA PARTIDA
def get_partida(partida_id: int):
    try:
        conn = db_client()
        cur = conn.cursor()

        cur.execute("SELECT * FROM partida WHERE ID = %s", (partida_id,))
        resultado = cur.fetchone()
    finally:
        conn.close()
    return resultado

def create_partida(intents: int):
    try:
        conn = db_client()
        cur = conn.cursor()

        sql = "INSERT INTO partida (intents) VALUES (%s)"
        values = (intents,)
        cur.execute(sql, values)
        conn.commit()
    finally:
        conn.close()

def update_partida(partida_id: int, intents: int):
    try:
        conn = db_client()
        cur = conn.cursor()

        cur.execute("UPDATE partida SET intents = %s WHERE ID = %s", (intents, partida_id))
        conn.commit()
    finally:
        conn.close()

def delete_partida(partida_id: int):
    try:
        conn = db_client()
        cur = conn.cursor()

        cur.execute("DELETE FROM partida WHERE ID = %s", (partida_id,))
        conn.commit()
    finally:
        conn.close()

# CRUD PANTALLA
def get_pantalla(idioma: str):
    try:
        conn = db_client()
        cur = conn.cursor()

        cur.execute("SELECT frase FROM pantalla WHERE Idioma = %s", (idioma,))
        resultado = cur.fetchone()
    finally:
        conn.close()
    return resultado

def create_pantalla(Idioma: str, Frase: str):
    try:
        conn = db_client()
        cur = conn.cursor()

        sql = "INSERT INTO pantalla (Idioma, frase) VALUES (%s, %s)"
        values = (Idioma, Frase)
        cur.execute(sql, values)
        conn.commit()
    finally:
        conn.close()

def update_pantalla(Idioma: str, Frase: str):
    try:
        conn = db_client()
        cur = conn.cursor()

        cur.execute("UPDATE pantalla SET frase = %s WHERE Idioma = %s", (Frase, Idioma))
        conn.commit()
    finally:
        conn.close()

def delete_pantalla(Idioma: str):
    try:
        conn = db_client()
        cur = conn.cursor()

        cur.execute("DELETE FROM pantalla WHERE Idioma = %s", (Idioma,))
        conn.commit()
    finally:
        conn.close()

