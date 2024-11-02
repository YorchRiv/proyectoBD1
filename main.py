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

def seleccionar_tabla(accion):
    print(f"\n--- {accion} Registros ---")
    tablas = ["CICLOS", "DOCUMENTO", "ESTUDIANTES", "INSCRIPCIONES", "PAGOS_COLEGIATURAS", "VENTAS"]
    
    for i, tabla in enumerate(tablas, 1):
        print(f"{i}.) {tabla}")
    
    print(f"{len(tablas) + 1}.) Volver al menú principal")
    
    choice = input("Seleccione una tabla (1-6): ")
    
    if choice.isdigit() and 1 <= int(choice) <= len(tablas):
        tabla_seleccionada = tablas[int(choice) - 1]
        print(f"Has seleccionado {accion} para la tabla: {tabla_seleccionada}")
        if accion == "Leer" and tabla_seleccionada == "CICLOS":
            leer_colegiaturas(conn_oracle, 1)  # Llama a la función específica para CICLOS
        else:
            print("Error")
        input("Presiona Enter para continuar...")
    elif choice == str(len(tablas) + 1):
        return  # Regresa al menú principal
    else:
        print("Opción no válida. Por favor, selecciona de nuevo.")
        input("Presiona Enter para continuar...")


def mostrar_menu_principal():
    while True:
        limpiar_consola()  # Limpia la consola al iniciar
        print("Proyecto Final de Base de Datos I")
        print("Menú Principal")
        print("dev: @yorchriv")
        print("")
        print("Seleccione una opción:")
        print("1.) Crear Registros")
        print("2.) Leer Datos")
        print("3.) Actualizar Datos")
        print("4.) Eliminar Datos")
        print("5.) Salir")

        choice = input("Seleccione una opción (1-5): ")

        if choice == '1':
            seleccionar_tabla("Crear")
        elif choice == '2':
            seleccionar_tabla("Leer")
        elif choice == '3':
            seleccionar_tabla("Actualizar")
        elif choice == '4':
            seleccionar_tabla("Eliminar")
        elif choice == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, selecciona de nuevo.")

if __name__ == "__main__":
    limpiar_consola()  # Limpia la consola al iniciar
    print ("Proyecto Final de Base de Datos I")
    print ("Modulo Colegiaturas")
    print ("dev: @yorchriv")

    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")

    # Llama a la función para verificar el usuario
    if verificar_usuario(usuario, contraseña, connection_string):        
        conn_oracle = conectar_oracle()                    

        mostrar_menu_principal()
        conn_oracle.close()  # Cierra la conexión después de usarla
        