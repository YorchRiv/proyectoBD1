#CREATE
def insertar_ciclo(conn, año=None, descripcion=None):
    cursor = conn.cursor()
    sql = """
        INSERT INTO CICLOS (AÑO, DESCRIPCION)
        VALUES (:1, :2)
    """
    try:
        cursor.execute(sql, (año, descripcion))
        conn.commit()
        print("Ciclo insertado correctamente.")
    except Exception as e:
        print(f"Error al insertar ciclo: {e}")
    finally:
        cursor.close()

def insertar_documento(conn, tipo_documento, fecha_emision, serie_fel, dte_fel, monto, id_pago):
    cursor = conn.cursor()
    sql = """
        INSERT INTO DOCUMENTO (TIPO_DOCUMENTO, FECHA_EMISION, SERIE_FEL, DTE_FEL, MONTO, ID_PAGO)
        VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD'), :3, :4, :5, :6)
    """
    try:
        cursor.execute(sql, (tipo_documento, fecha_emision, serie_fel, dte_fel, monto, id_pago))
        conn.commit()
        print("Documento insertado correctamente.")
    except Exception as e:
        print(f"Error al insertar documento: {e}")
    finally:
        cursor.close()

def insertar_estudiante(conn, nombre=None, codigo_mineduc=None, grado=None, seccion=None):
    cursor = conn.cursor()
    sql = """
        INSERT INTO ESTUDIANTES (NOMBRE, CODIGO_MINEDUC, GRADO, SECCION)
        VALUES (:1, :2, :3, :4)
    """
    try:
        cursor.execute(sql, (nombre, codigo_mineduc, grado, seccion))
        conn.commit()
        print("Estudiante insertado correctamente.")
    except Exception as e:
        print(f"Error al insertar estudiante: {e}")
    finally:
        cursor.close()

def insertar_inscripcion(conn, fecha_inscripcion=None, grado=None, seccion=None, mes=None, monto=None, id_estudiante=None, id_ciclo=None):
    cursor = conn.cursor()
    sql = """
        INSERT INTO INSCRIPCIONES (FECHA_INSCRIPCION, GRADO, SECCION, MES, MONTO, ID_ESTUDIANTE, ID_CICLO)
        VALUES (TO_DATE(:1, 'YYYY-MM-DD'), :2, :3, :4, :5, :6, :7)
    """
    try:
        cursor.execute(sql, (fecha_inscripcion, grado, seccion, mes, monto, id_estudiante, id_ciclo))
        conn.commit()
        print("Inscripción insertada correctamente.")
    except Exception as e:
        print(f"Error al insertar inscripción: {e}")
    finally:
        cursor.close()

def insertar_pago_colegiatura(conn, monto=None, fecha_pago=None, tipo_pago=None, id_estudiante=None, id_inscripcion=None):
    cursor = conn.cursor()
    sql = """
        INSERT INTO PAGOS_COLEGIATURAS (MONTO, FECHA_PAGO, TIPO_PAGO, ID_ESTUDIANTE, ID_INSCRIPCION)
        VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD'), :3, :4, :5)
    """
    try:
        cursor.execute(sql, (monto, fecha_pago, tipo_pago, id_estudiante, id_inscripcion))
        conn.commit()
        print("Pago de colegiatura insertado correctamente.")
    except Exception as e:
        print(f"Error al insertar pago de colegiatura: {e}")
    finally:
        cursor.close()

def insertar_venta(conn, producto=None, cantidad=None, precio=None, id_estudiante=None):
    cursor = conn.cursor()
    sql = """
        INSERT INTO VENTAS (PRODUCTO, CANTIDAD, PRECIO, ID_ESTUDIANTE)
        VALUES (:1, :2, :3, :4)
    """
    try:
        cursor.execute(sql, (producto, cantidad, precio, id_estudiante))
        conn.commit()
        print("Venta insertada correctamente.")
    except Exception as e:
        print(f"Error al insertar venta: {e}")
    finally:
        cursor.close()


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

#UPDATE
