import os
import getpass
from auth import verificar_usuario
from db_oracle import conectar_oracle
from crud import *

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
        if accion == "Leer":
            if tabla_seleccionada == "CICLOS":
                leer_colegiaturas(conn_oracle, 1)  # Llama a leer_colegiaturas para CICLOS
            elif tabla_seleccionada == "DOCUMENTO":
                leer_colegiaturas(conn_oracle, 2)  
            elif tabla_seleccionada == "ESTUDIANTES":
                leer_colegiaturas(conn_oracle, 3)  
            elif tabla_seleccionada == "INSCRIPCIONES":
                leer_colegiaturas(conn_oracle, 4)  
            elif tabla_seleccionada == "PAGOS_COLEGIATURAS":
                leer_colegiaturas(conn_oracle, 5)
            elif tabla_seleccionada == "VENTAS":
                leer_colegiaturas(conn_oracle, 6)
            else:
                print("Error")

        elif accion == "Crear":
            if tabla_seleccionada == "CICLOS":
                año = int(input("Ingrese el año del ciclo: "))
                descripcion = input("Ingrese la descripción del ciclo: ")
                insertar_ciclo(conn_oracle, año=año, descripcion=descripcion)

            elif tabla_seleccionada == "DOCUMENTO":
                tipo_documento = input("Ingrese el tipo de documento: ")
                fecha_emision = input("Ingrese la fecha de emisión (YYYY-MM-DD): ")
                serie_fel = input("Ingrese la serie FEL: ")
                dte_fel = input("Ingrese el DTE FEL: ")
                monto = float(input("Ingrese el monto: "))
                id_pago = int(input("Ingrese el ID de pago: "))
                insertar_documento(conn_oracle, tipo_documento=tipo_documento, fecha_emision=fecha_emision, serie_fel=serie_fel, dte_fel=dte_fel, monto=monto, id_pago=id_pago)

            elif tabla_seleccionada == "ESTUDIANTES":
                nombre = input("Ingrese el nombre del estudiante: ")
                codigo_mineduc = input("Ingrese el código MINEDUC: ")
                grado = input("Ingrese el grado: ")
                seccion = input("Ingrese la sección: ")
                insertar_estudiante(conn_oracle, nombre=nombre, codigo_mineduc=codigo_mineduc, grado=grado, seccion=seccion)

            elif tabla_seleccionada == "INSCRIPCIONES":
                fecha_inscripcion = input("Ingrese la fecha de inscripción (YYYY-MM-DD): ")
                grado = input("Ingrese el grado: ")
                seccion = input("Ingrese la sección: ")
                mes = input("Ingrese el mes de la inscripción: ")
                monto = float(input("Ingrese el monto: "))
                id_estudiante = int(input("Ingrese el ID del estudiante: "))
                id_ciclo = int(input("Ingrese el ID del ciclo: "))
                insertar_inscripcion(conn_oracle, fecha_inscripcion=fecha_inscripcion, grado=grado, seccion=seccion, mes=mes, monto=monto, id_estudiante=id_estudiante, id_ciclo=id_ciclo)

            elif tabla_seleccionada == "PAGOS_COLEGIATURAS":
                monto = float(input("Ingrese el monto del pago: "))
                fecha_pago = input("Ingrese la fecha de pago (YYYY-MM-DD): ")
                tipo_pago = input("Ingrese el tipo de pago: ")
                id_estudiante = int(input("Ingrese el ID del estudiante: "))
                id_inscripcion = int(input("Ingrese el ID de inscripción: "))
                insertar_pago_colegiatura(conn_oracle, monto=monto, fecha_pago=fecha_pago, tipo_pago=tipo_pago, id_estudiante=id_estudiante, id_inscripcion=id_inscripcion)

            elif tabla_seleccionada == "VENTAS":
                producto = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                id_estudiante = int(input("Ingrese el ID del estudiante: "))
                insertar_venta(conn_oracle, producto=producto, cantidad=cantidad, precio=precio, id_estudiante=id_estudiante)

            else:
                print("Error")
        
        elif accion == "Actualizar":
            if tabla_seleccionada == "CICLOS":
                id_ciclo = int(input("Ingrese el ID del ciclo a actualizar: "))
                mostrar_datos_antiguos(conn_oracle, "CICLOS", id_ciclo, "ID_CICLO")  # Asegúrate de que este sea el nombre correcto de la columna
                año = int(input("Ingrese el nuevo año del ciclo: "))
                descripcion = input("Ingrese la nueva descripción del ciclo: ")
                actualizar_ciclo(conn_oracle, id_ciclo, año=año, descripcion=descripcion)

            elif tabla_seleccionada == "DOCUMENTO":
                id_documento = int(input("Ingrese el ID del documento a actualizar: "))
                mostrar_datos_antiguos(conn_oracle, "DOCUMENTO", id_documento, "ID_DOCUMENTO")  # Asegúrate de que este sea el nombre correcto de la columna
                tipo_documento = input("Ingrese el nuevo tipo de documento: ")
                fecha_emision = input("Ingrese la nueva fecha de emisión (YYYY-MM-DD): ")
                serie_fel = input("Ingrese la nueva serie FEL: ")
                dte_fel = input("Ingrese el nuevo DTE FEL: ")
                monto = float(input("Ingrese el nuevo monto: "))
                id_pago = int(input("Ingrese el nuevo ID de pago: "))
                actualizar_documento(conn_oracle, id_documento, tipo_documento=tipo_documento, fecha_emision=fecha_emision, serie_fel=serie_fel, dte_fel=dte_fel, monto=monto, id_pago=id_pago)

            elif tabla_seleccionada == "ESTUDIANTES":
                id_estudiante = int(input("Ingrese el ID del estudiante a actualizar: "))
                mostrar_datos_antiguos(conn_oracle, "ESTUDIANTES", id_estudiante, "ID_ESTUDIANTE")
                nombre = input("Ingrese el nuevo nombre del estudiante: ")
                codigo_mineduc = input("Ingrese el nuevo código MINEDUC: ")
                grado = input("Ingrese el nuevo grado: ")
                seccion = input("Ingrese la nueva sección: ")
                actualizar_estudiante(conn_oracle, id_estudiante, nombre=nombre, codigo_mineduc=codigo_mineduc, grado=grado, seccion=seccion)

            elif tabla_seleccionada == "INSCRIPCIONES":
                id_inscripcion = int(input("Ingrese el ID de inscripción a actualizar: "))
                mostrar_datos_antiguos(conn_oracle, "INSCRIPCIONES", id_inscripcion, "ID_INSCRIPCION")
                fecha_inscripcion = input("Ingrese la nueva fecha de inscripción (YYYY-MM-DD): ")
                grado = input("Ingrese el nuevo grado: ")
                seccion = input("Ingrese la nueva sección: ")
                mes = input("Ingrese el nuevo mes de la inscripción: ")
                monto = float(input("Ingrese el nuevo monto: "))
                id_estudiante = int(input("Ingrese el nuevo ID del estudiante: "))
                id_ciclo = int(input("Ingrese el nuevo ID del ciclo: "))
                actualizar_inscripcion(conn_oracle, id_inscripcion, fecha_inscripcion=fecha_inscripcion, grado=grado, seccion=seccion, mes=mes, monto=monto, id_estudiante=id_estudiante, id_ciclo=id_ciclo)

            elif tabla_seleccionada == "PAGOS_COLEGIATURAS":
                id_pago_colegiatura = int(input("Ingrese el ID del pago de colegiatura a actualizar: "))
                mostrar_datos_antiguos(conn_oracle, "PAGOS_COLEGIATURAS", id_pago_colegiatura, "ID_PAGO_COLEGIATURA")  # Asegúrate de que este sea el nombre correcto de la columna
                monto = float(input("Ingrese el nuevo monto del pago: "))
                fecha_pago = input("Ingrese la nueva fecha de pago (YYYY-MM-DD): ")
                tipo_pago = input("Ingrese el nuevo tipo de pago: ")
                id_estudiante = int(input("Ingrese el nuevo ID del estudiante: "))
                id_inscripcion = int(input("Ingrese el nuevo ID de inscripción: "))
                actualizar_pago_colegiatura(conn_oracle, id_pago_colegiatura, monto=monto, fecha_pago=fecha_pago, tipo_pago=tipo_pago, id_estudiante=id_estudiante, id_inscripcion=id_inscripcion)

            elif tabla_seleccionada == "VENTAS":
                id_venta = int(input("Ingrese el ID de la venta a actualizar: "))
                mostrar_datos_antiguos(conn_oracle, "VENTAS", id_venta, "ID_VENTA")  # Asegúrate de que este sea el nombre correcto de la columna
                producto = input("Ingrese el nuevo nombre del producto: ")
                cantidad = int(input("Ingrese la nueva cantidad: "))
                precio = float(input("Ingrese el nuevo precio: "))
                id_estudiante = int(input("Ingrese el nuevo ID del estudiante: "))
                actualizar_venta(conn_oracle, id_venta, producto=producto, cantidad=cantidad, precio=precio, id_estudiante=id_estudiante)

            else:
                print("Error: tabla no válida.")

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
        