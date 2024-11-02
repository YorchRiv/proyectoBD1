import os
import getpass
from auth import verificar_usuario
from db_oracle import conectar_oracle
from crud import leer_colegiaturas

# Credenciales
server = 'localhost'
database = 'COLEGIO'
username = 'USUARIO_DBA'
password = 'serverSQL'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

def limpiar_consola():
    # Comando para limpiar la consola, funciona en Windows y en Unix
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_menu_principal():
    limpiar_consola()  # Limpia la consola al iniciar
    print("Proyecto Final de Base de Datos I")
    print("Menu Principal")
    print("dev: @yorchriv")
    print("")
    print("Seleccione una opción:")
    print("1.) Crear Registros")
    print("2.) Leer Datos")
    print("3.) Actualizar Datos")
    print("4.) Eliminar Datos")
    print("5.) Salir")

if __name__ == "__main__":
    limpiar_consola()  # Limpia la consola al iniciar
    print ("Proyecto Final de Base de Datos I")
    print ("Modulo Colegiaturas")
    print ("dev: @yorchriv")

    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")

    # Llama a la función para verificar el usuario
    if verificar_usuario(usuario, contraseña, connection_string):
        while True:
            limpiar_consola()  # Limpia la consola para el menú
            conn_oracle = conectar_oracle()

            mostrar_menu_principal()

            opcion = input("Ingrese la opción deseada: ")

            if opcion == '1':
                #crear_registro_colegiaturas(conn_oracle)
                print("Opcion 1")
            elif opcion == '2':
                leer_colegiaturas(conn_oracle)
                print("Presiona Enter para continuar...")
                input() 
            elif opcion == '3':
                #actualizar_registro_colegiaturas(conn_oracle)
                print("Opcion 3")
            elif opcion == '4':
                #eliminar_registro_colegiaturas(conn_oracle)
                print("Opcion 3")
            elif opcion == '5':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        conn_oracle = conectar_oracle()
        leer_colegiaturas(conn_oracle)
        conn_oracle.close()  # Cierra la conexión después de usarla
        