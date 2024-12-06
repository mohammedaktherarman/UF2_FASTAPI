from fastapi import FastAPI
from db import intents, pillafrase
app = FastAPI()

@app.get("/frase/{Idioma}")
def show_alumne(Idioma: str):  
    return {"frase" :pillafrase(Idioma)}

@app.post("/partida/{partida_id}/fallo")
def fallo_partida(partida_id: int):
    return {"numero de intents": intents(partida_id)}