#READ
def leer_colegiaturas(conn):
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM ESTUDIANTES"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)  # Imprime cada fila de resultados
    except Exception as e:
        print("Error al leer datos:", e)
    finally:
        cursor.close()
