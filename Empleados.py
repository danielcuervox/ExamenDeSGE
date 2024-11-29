import random

from sqlalchemy import Boolean
from log import log
from Administrador import Administrador
from Recepcionista import Recepcionista
class Empleados:
    empleados = []


    def busar_empleado(self) -> Boolean:
        logger = log()
        acceso_valido = False
        print("== LISTA TODOS LOS EMPLEADOS ==")
        for emple in self.empleados:
            print(emple)

        try:

            nom_emple = input("escribe tu nombre de empleado")
            #se busca dentro de todos los empledos

            for empleado in self.empleados:

                if empleado.nick.lower() == nom_emple.lower():  # Permitir coincidencias sin importar mayúsculas/minúsculas
                    print("Acceso concedido")
                    acceso_valido = True

            return acceso_valido

        except:
            logger.escribir_fichero("no ha podido verificar la info", "ERROR")


    def cargar_empleados(self):
        lista_nombres = ["Tom", "Jose", "Camilo", "Joserra", "Daniel", "Manuel", "Mariano"]
        lista_correos = ["algo@correo.com", "otro@correo.com", "masalgo@correo.com", "generalalgo@correo.com"]

        for i in range(10):
            nick = random.choice(lista_nombres)
            correo = random.choice(lista_correos)
            tipo_emple = random.choice([1, 2,])

            if tipo_emple == 1:
                nuevo_admin = Administrador(nick, correo)
                self.empleados.append(nuevo_admin)

            elif tipo_emple == 2:
                nuevo_franco = Recepcionista(nick, correo)
                self.empleados.append(nuevo_franco)
