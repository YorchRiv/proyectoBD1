#READ
def leer_colegiaturas(conn, tabla_num):
    try:
        cursor = conn.cursor()
        # Mapeo de números a nombres de tablas
        tablas = {
            1: "CICLOS",
            2: "DOCUMENTO",
            3: "ESTUDIANTES",
            4: "INSCRIPCIONES",
            5: "PAGOS_COLEGIATURAS",
            6: "VENTAS"
        }
        
        # Verifica si el número corresponde a una tabla válida
        if tabla_num in tablas:
            query = f"SELECT * FROM {tablas[tabla_num]}"
            cursor.execute(query)
            resultados = cursor.fetchall()
            for row in resultados:
                print(row)  # Imprime cada fila de resultados
        else:
            print("Número de tabla no válido. Debe ser un número entre 1 y 6.")
            
    except Exception as e:
        print("Error al leer datos:", e)
    finally:
        cursor.close()
