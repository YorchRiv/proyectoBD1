import pyodbc

def conectar_db(connection_string):
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None

def verificar_usuario(nombre_usuario, password, connection_string):
    conn = conectar_db(connection_string)
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT id_usuario FROM SEGURIDAD_COLEGIO.usuarios WHERE nombre_usuario = ? AND password = ?"
            cursor.execute(query, (nombre_usuario, password))
            resultado = cursor.fetchone()
            if resultado:
                print("Inicio de sesión exitoso")
                return True
            else:
                print("Credenciales incorrectas")
                return False
        except Exception as e:
            print("Error al verificar el usuario:", e)
        finally:
            conn.close()
    return False
