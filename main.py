from auth import verificar_usuario

# Configura tus parámetros de conexión
server = 'localhost'
database = 'COLEGIO'
username = 'USUARIO_DBA'
password = 'serverSQL'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

if __name__ == "__main__":
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    # Llama a la función para verificar el usuario
    verificar_usuario(usuario, contraseña, connection_string)
