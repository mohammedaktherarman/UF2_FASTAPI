from connection import db_client
from fastapi import FastAPI

app = FastAPI()

def pillafrase(Idioma: str):
    try:
        conn = db_client() 
        cur = conn.cursor()

        cur.execute("SELECT frase FROM pantalla WHERE Idioma = %s", (Idioma,))
        frase = cur.fetchall()  
    finally:
        conn.close()

    return frase

@app.get("/frase/{Idioma}")
def show_alumne(Idioma: str):  
    frase = pillafrase(Idioma)

    if not frase:  
        return {"message": "No hi ha frase"}

    return {"frase": frase}
