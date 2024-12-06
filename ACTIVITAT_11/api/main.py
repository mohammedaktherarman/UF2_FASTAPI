from fastapi import FastAPI
from db import intents, pillafrase, abecedari, jugador
app = FastAPI()

@app.get("/frase/{Idioma}")
def endpointfrase(Idioma: str):  
    return {"frase" :pillafrase(Idioma)}

@app.post("/partida/{partida_id}/intents")
def endpointnumerodeintents(partida_id: int):
    return {"numero de intents": intents(partida_id)}

@app.get("/abecedari/{idioma}")
def endpointabecedari(idioma: str):
    return {"idioma": idioma, "abecedari": abecedari(idioma)}

@app.get("/jugador/{jugador_id}")
def endpointjugador(jugador_id: int):
    dades = jugador(jugador_id)

    return {
        "ID": jugador_id,
        "Nom": dades[0],
        "Total_partides": dades[1],
        "Partides_ganadas": dades[2],
        "Partides_mes_punts": dades[3],
        "Punts_partida_actual": dades[4],
    }