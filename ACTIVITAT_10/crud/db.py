from db_connect.connection import conexio  

def getTemas():
    conn = conexio()
    cursor = conn.cursor()
    
    cursor.execute("SELECT DISTINCT theme FROM paraules")
    themes = cursor.fetchall()  

    conn.close()

    result = []
    for theme in themes:
        result.append({"option": theme[0]})
    
    return result

def getParaula(theme: str):
    conn = conexio()
    cursor = conn.cursor()

    cursor.execute("SELECT word FROM paraules WHERE theme = %s ORDER BY RANDOM() LIMIT 1", (theme,))
    paraula = cursor.fetchone()  

    conn.close()

    if paraula:
        return [{"option": paraula[0]}]  
    
    return [] 