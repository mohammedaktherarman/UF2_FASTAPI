import pandas as pd
import psycopg2
from connection import conexio

# Per executa aquest codi tens que esta dins de la carpeta insertDATA en la terminal per executa script.py

readedDocument = pd.read_csv("arxiu.csv")
processedDocument = readedDocument.to_dict(orient="list")

# agafo per columnes i la converteix en una llista de valors

words = processedDocument['WORD']
themes = processedDocument['THEME']

#Funcio on agafa el word y el theme de cada fila y la inserta a la taula en la DB amb la query la taula la he anomenada "paraules"

def creaRegistre(word: str, theme: str):
    try:
        conn = conexio()
        cursor = conn.cursor()

        sql = '''insert into paraules (word, theme) values (%s, %s)'''

        values = (word, theme)
        
        cursor.execute(sql, values)
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        conn.close()

#Bucle on inserto totes una a una 
for word, theme in zip(words, themes):
    creaRegistre(word, theme)
