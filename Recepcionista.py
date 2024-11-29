from Empleado import Empleado
#import ...

class Recepcionista(Empleado):
    def __init__(self,  nick = "recepcionista", correo = "recep@gmail.com", num_consultas = 0):
        super().__init__(nick, correo)
        self.nick = nick
        self.correo = correo
        self.num_consultas = num_consultas

    def __str__(self):
        return super().__str__() + f", num_consultas: {self.num_consultas}"