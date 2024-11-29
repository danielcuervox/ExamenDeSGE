import pandas as pd

import constantes as cons
import db
from Empleados import Empleados
from sqlalchemy import text, Boolean
from Empleados import Empleados
from log import log

def conexion():
    db_config = {
        'dbname': cons.dbname,
        'user': cons.user,
        'password': cons.password,
        'host': cons.host,
        'port': cons.port,
    }
    return db_config

def crearConexion():
    db_config = conexion()
    db_connection = db.PostgreSQLConnection(**db_config)
    db_connection.connect()
    return db_connection


def verficar_info_emple() -> Boolean:
    acceso = False
    empleados.cargar_empleados()
    acceso = empleados.busar_empleado()

    return acceso


if __name__ == "__main__":
    db_connection = crearConexion()
    empleados = Empleados()
    #añadir aqui a los empleados el admin y el recepcionista
    #cada vez que se realice una actualización o una consulta se deberá sumar 1.
    logger = log()

    try:

        while True:
            print("\n--- MENÚ ---")
            print("1. Mostrar los vuelos de un cliente")
            print("2. Mostrar la dirección de un usuario")
            print("3. Vuelo de los pasajeros")
            print("4. Actualización de muertos")

            verficar_info_emple()

            try:
                if verficar_info_emple:
                    opcion = input("escribe la opción elegida")
                else:
                    print("Usuario no encontrado en la base de datos")

                if opcion == '1':
                    logger.escribir_fichero("CONSULTAR NOMBRE CLIENTES", "INFO")
                    query = text(cons.QUERY_CLIENTES_ACTIVOS)
                    resultQuery = db_connection.execute_query(query)
                    if (resultQuery):
                        print(resultQuery)
                        df = pd.DataFrame(resultQuery)

                elif opcion == '2':
                    logger.escribir_fichero("CONSULTA DE DIRECCION", "INFO")
                    query = text(cons.QUERY_DIRECCION)
                    resultQuery = db_connection.execute_query(query)
                    if (resultQuery):
                        print(resultQuery)
                elif opcion == '3':
                    logger.escribir_fichero("CONSULTA DE VUELO POR ID", "INFO")
                    ID = int(input("escribe el id del vuelo"))
                    query = text(cons.QUERY_SELECT_VUELO_BY_ID)
                    resultQuery = db_connection.execute_query(query, {'id': ID})
                    print(resultQuery)
                    df = pd.DataFrame(resultQuery)
                    print(df)
                else:
                    print("opción no valida")
                    logger.escribir_fichero("OPCIÓN INVALIDA", "ERROR")
            except:
                print("no ha podido verificar la info")
                logger.escribir_fichero("no ha podido verificar la info", "ERROR")

    except Exception as e:
        print(e)
        print("Error al insertar datos:", e)
    finally:
        db_connection.close()


