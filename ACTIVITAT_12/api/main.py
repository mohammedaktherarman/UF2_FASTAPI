from fastapi import FastAPI
from db import (get_jugador, create_jugador, update_jugador, delete_jugador, 
    get_paraula, create_paraula, delete_paraula, update_paraula,
    get_partida, create_partida, update_partida, delete_partida,
    get_pantalla, create_pantalla, update_pantalla, delete_pantalla )

app = FastAPI()

# ENDPOINTS TAULA JUGADOR
@app.get("/jugador/{jugador_id}")
def obtener_jugador(jugador_id: int):
    return get_jugador(jugador_id)

@app.post("/jugador/")
def crear_jugador(Nom: str, Total_partides: int, Partides_ganadas: int, Partides_amb_mes_punts: int, Punts_partida_actual: int):
    return {"id": create_jugador(Nom, Total_partides, Partides_ganadas, Partides_amb_mes_punts, Punts_partida_actual)}

@app.put("/jugador/{jugador_id}")
def actualizar_jugador(jugador_id: int, Nom: str, Total_partides: int, Partides_ganadas: int, Partides_amb_mes_punts: int, Punts_partida_actual: int):
    update_jugador(jugador_id, Nom, Total_partides, Partides_ganadas, Partides_amb_mes_punts, Punts_partida_actual)
    return {"Jugador actualitzat"}

@app.delete("/jugador/{jugador_id}")
def borrar_jugador(jugador_id: int):
    delete_jugador(jugador_id)
    return {"Jugador borrat"}

# ENDPOINTS TAULA PARAULES
@app.get("/paraules/{paraula}")
def obtener_paraula(paraula: str):
    return get_paraula(paraula)

@app.post("/paraules/")
def crear_paraula(paraula: str, theme: str):
    return {create_paraula(paraula, theme)}

@app.put("/paraules/{paraula}")
def actualizar_paraula(paraula: str, theme: str):
    update_paraula(paraula, theme)
    return {"Paraula actualitzada"}

@app.delete("/paraules/{paraula}")
def borrar_paraula(paraula: str):
    delete_paraula(paraula)
    return {"Paraula borrat"}

# ENDPOINTS TAULA PARTIDA
@app.get("/partida/{partida_id}")
def obtener_partida(partida_id: int):
    return get_partida(partida_id)

@app.post("/partida/")
def crear_partida(intents: int):
    return {create_partida(intents)}

@app.put("/partida/{partida_id}")
def actualizar_intentos(partida_id: int, intents: int):
    update_partida(partida_id, intents)
    return {"Partida actualitzat"}

@app.delete("/partida/{partida_id}")
def borrar_partida(partida_id: int):
    delete_partida(partida_id)
    return {"Partida borrat"}

# ENDPOINTS TAULA PANTALLA
@app.get("/pantalla/{idioma}")
def obtener_pantalla(idioma: str):
    return get_pantalla(idioma)

@app.post("/pantalla/")
def crear_pantalla(Idioma: str, Frase: str):
    return {create_pantalla(Idioma, Frase)}

@app.put("/pantalla/{idioma}")
def actualizar_pantalla(idioma: str, Frase: str):
    update_pantalla(idioma, Frase)
    return {"Pantalla actualitzat"}

@app.delete("/pantalla/{idioma}")
def borrar_pantalla(idioma: str):
    delete_pantalla(idioma)
    return {"Pantalla borrat"}
