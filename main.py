import os
import getpass
from auth import verificar_usuario

def limpiar_consola():
    # Comando para limpiar la consola, funciona en Windows y en Unix
    os.system('cls' if os.name == 'nt' else 'clear')

# Configura tus parámetros de conexión
server = 'localhost'
database = 'COLEGIO'
username = 'USUARIO_DBA'
password = 'serverSQL'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

if __name__ == "__main__":
    limpiar_consola()  # Limpia la consola al iniciar
    print ("Proyecto Final de Base de Datos I")
    print ("Modulo Colegiaturas")
    print ("dev: @yorchriv")
    print ("")
    usuario = input("Ingrese su nombre de usuario: ")
    
    # Usar getpass para ingresar la contraseña de manera oculta
    contraseña = getpass.getpass("Ingrese su contraseña: ")

    # Llama a la función para verificar el usuario
    verificar_usuario(usuario, contraseña, connection_string)