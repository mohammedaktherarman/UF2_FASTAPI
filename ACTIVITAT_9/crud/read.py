from db_connect.connection import conexio
import psycopg2


def read_users():
    try:
        conn = conexio()
        cursor = conn.cursor()
        cursor.execute("select * from USERS")
        registres = cursor.fetchall()

        users = []

        for registre in registres:
            user_dict = {
                "user_id": registre[0],
                "user_name": registre[1],
                "user_surname": registre[2],
                "user_age": registre[3],
                "user_email": registre[4],
            }
            users.append(user_dict)

        return users

    except (Exception, psycopg2.Error) as error:
        return {"error": str(error)}

    finally:
        if conn:
            conn.close()
