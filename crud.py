def mostrar_datos_antiguos(conn, tabla, id_registro, id_columna):
    cursor = conn.cursor()
    sql = f"SELECT * FROM {tabla} WHERE {id_columna} = :1"  # Solo el nombre de la tabla sin esquema
    cursor.execute(sql, (id_registro,))
    datos = cursor.fetchone()
    cursor.close()
    
    if datos:
        print("Datos antiguos:")
        print(datos)
    else:
        print("No se encontraron registros para el ID proporcionado.")


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
def actualizar_ciclo(conn, id_ciclo, año=None, descripcion=None):
    cursor = conn.cursor()
    sql = """
        UPDATE USUARIO_DBA.CICLOS
        SET AÑO = NVL(:1, AÑO), DESCRIPCION = NVL(:2, DESCRIPCION)
        WHERE ID_CICLO = :3
    """
    try:
        cursor.execute(sql, (año, descripcion, id_ciclo))
        conn.commit()
        print("Ciclo actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar ciclo: {e}")
    finally:
        cursor.close()

def actualizar_documento(conn, id_documento, tipo_documento=None, fecha_emision=None, serie_fel=None, dte_fel=None, monto=None, id_pago=None):
    cursor = conn.cursor()
    sql = """
        UPDATE DOCUMENTO
        SET TIPO_DOCUMENTO = NVL(:1, TIPO_DOCUMENTO),
            FECHA_EMISION = NVL(TO_DATE(:2, 'YYYY-MM-DD'), FECHA_EMISION),
            SERIE_FEL = NVL(:3, SERIE_FEL),
            DTE_FEL = NVL(:4, DTE_FEL),
            MONTO = NVL(:5, MONTO),
            ID_PAGO = NVL(:6, ID_PAGO)
        WHERE ID_DOCUMENTO = :7
    """
    try:
        cursor.execute(sql, (tipo_documento, fecha_emision, serie_fel, dte_fel, monto, id_pago, id_documento))
        conn.commit()
        print("Documento actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar documento: {e}")
    finally:
        cursor.close()

def actualizar_estudiante(conn, id_estudiante, nombre=None, codigo_mineduc=None, grado=None, seccion=None):
    cursor = conn.cursor()
    sql = """
        UPDATE USUARIO_DBA.ESTUDIANTES
        SET NOMBRE = NVL(:1, NOMBRE),
            CODIGO_MINEDUC = NVL(:2, CODIGO_MINEDUC),
            GRADO = NVL(:3, GRADO),
            SECCION = NVL(:4, SECCION)
        WHERE ID_ESTUDIANTE = :5
    """
    try:
        cursor.execute(sql, (nombre, codigo_mineduc, grado, seccion, id_estudiante))
        conn.commit()
        print("Estudiante actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar estudiante: {e}")
    finally:
        cursor.close()

def actualizar_inscripcion(conn, id_inscripcion, fecha_inscripcion=None, grado=None, seccion=None, mes=None, monto=None, id_estudiante=None, id_ciclo=None):
    cursor = conn.cursor()
    sql = """
        UPDATE USUARIO_DBA.INSCRIPCIONES
        SET FECHA_INSCRIPCION = NVL(TO_DATE(:1, 'YYYY-MM-DD'), FECHA_INSCRIPCION),
            GRADO = NVL(:2, GRADO),
            SECCION = NVL(:3, SECCION),
            MES = NVL(:4, MES),
            MONTO = NVL(:5, MONTO),
            ID_ESTUDIANTE = NVL(:6, ID_ESTUDIANTE),
            ID_CICLO = NVL(:7, ID_CICLO)
        WHERE ID_INSCRIPCION = :8
    """
    try:
        cursor.execute(sql, (fecha_inscripcion, grado, seccion, mes, monto, id_estudiante, id_ciclo, id_inscripcion))
        conn.commit()
        print("Inscripción actualizada correctamente.")
    except Exception as e:
        print(f"Error al actualizar inscripción: {e}")
    finally:
        cursor.close()

def actualizar_pago_colegiatura(conn, id_pago, monto=None, fecha_pago=None, tipo_pago=None, id_estudiante=None, id_inscripcion=None):
    cursor = conn.cursor()
    sql = """
        UPDATE USUARIO_DBA.PAGOS_COLEGIATURAS
        SET MONTO = NVL(:1, MONTO),
            FECHA_PAGO = NVL(TO_DATE(:2, 'YYYY-MM-DD'), FECHA_PAGO),
            TIPO_PAGO = NVL(:3, TIPO_PAGO),
            ID_ESTUDIANTE = NVL(:4, ID_ESTUDIANTE),
            ID_INSCRIPCION = NVL(:5, ID_INSCRIPCION)
        WHERE ID_PAGO = :6
    """
    try:
        cursor.execute(sql, (monto, fecha_pago, tipo_pago, id_estudiante, id_inscripcion, id_pago))
        conn.commit()
        print("Pago de colegiatura actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar pago de colegiatura: {e}")
    finally:
        cursor.close()

def actualizar_venta(conn, id_venta, producto=None, cantidad=None, precio=None, id_estudiante=None):
    cursor = conn.cursor()
    sql = """
        UPDATE USUARIO_DBA.VENTAS
        SET PRODUCTO = NVL(:1, PRODUCTO),
            CANTIDAD = NVL(:2, CANTIDAD),
            PRECIO = NVL(:3, PRECIO),
            ID_ESTUDIANTE = NVL(:4, ID_ESTUDIANTE)
        WHERE ID_VENTA = :5
    """
    try:
        cursor.execute(sql, (producto, cantidad, precio, id_estudiante, id_venta))
        conn.commit()
        print("Venta actualizada correctamente.")
    except Exception as e:
        print(f"Error al actualizar venta: {e}")
    finally:
        cursor.close()
