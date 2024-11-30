from fastapi import FastAPI, HTTPException
from typing import List
from schemas.schema import Tematica, Paraula
from crud.db import getTemas, getParaula

app = FastAPI()

@app.get("/penjat/tematica/opcions", response_model=List[Tematica])
async def get_options():
    try:

        temas = getTemas()

        return temas
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error")

@app.get("/penjat/tematica/{option}", response_model=List[Paraula])
async def get_word(option: str):
    try:

        paraula = getParaula(option)
        
        return paraula
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error")
