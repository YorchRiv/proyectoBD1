import pyodbc

# Configura tus parámetros de conexión
server = 'localhost'  # Por ejemplo, 'localhost' o '192.168.1.1'
database = 'COLEGIO'  # Por ejemplo, 'SEGURIDAD_COLEGIO'
username = 'USUARIO_DBA'  # Nombre de usuario para la conexión
password = 'serverSQL'  # Contraseña del usuario

# Establece la conexión
try:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(connection_string)
    print("Conexión exitosa")
except Exception as e:
    print("Error al conectar:", e)

# Asegúrate de cerrar la conexión cuando termines
finally:
    if 'conn' in locals():
        conn.close()

##INTERACCION

def verificar_usuario(nombre_usuario, password):
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        # Consulta para verificar el usuario y la contraseña
        query = "SELECT id_usuario FROM SEGURIDAD_COLEGIO.usuarios WHERE nombre_usuario = ? AND password = ?"
        cursor.execute(query, (nombre_usuario, password))  # Usa parámetros para evitar inyecciones SQL
        
        # Obtiene el resultado
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
        if 'conn' in locals():
            conn.close()
