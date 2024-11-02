import oracledb

def conectar_oracle():
    try:
        # Cambia estos parámetros según tu configuración
        conn = oracledb.connect(
            user='USUARIO_CRUD',
            password='Sistemas10*',
            dsn='localhost/XE'  # Asegúrate de que el DSN es correcto
        )
        print("Conexión exitosa a Oracle")
        return conn
    except oracledb.DatabaseError as e:
        print("Error al conectar a la base de datos Oracle:", e)
        return None
