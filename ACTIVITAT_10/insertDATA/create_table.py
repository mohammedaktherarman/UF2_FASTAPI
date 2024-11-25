import psycopg2
from connection import conexio


# Funcio per la creacio de la tabla 

def crearTabla():
    try:
        conn = conexio()

        cursor = conn.cursor()

        sql = '''CREATE TABLE PARAULES(
                        word VARCHAR(255) NOT NULL, 
                        theme VARCHAR(255) NOT NULL
        )'''

        cursor.execute(sql)
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        conn.close()

crearTabla()