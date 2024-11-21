from fastapi import FastAPI
from connection import conexio
from schema import User
import psycopg2

app = FastAPI()

@app.get("/users/", response_model=list[User])
def read_users():
    try:
        conn = conexio()
        cursor = conn.cursor()
        cursor.execute(" select * from users")
        registros = cursor.fetchall()

        users = []

        for registro in registros:
            user_dict = {
                "user_id": registro[0],
                "user_name": registro[1],
                "user_surname": registro[2],
                "user_age": registro[3],
                "user_email": registro[4],
            }
            users.append(user_dict)

        return users

    except (Exception, psycopg2.Error) as error:
        return {"error": str(error)}

    finally:
        conn.close()