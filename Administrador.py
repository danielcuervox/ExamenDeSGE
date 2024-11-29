from Empleado import Empleado
# import ...
class Administrador(Empleado):

    def __init__(self, nick = "admin", correo = "admin@admin.com" , num_actualizaciones = 0):
        super().__init__(nick, correo)
        self.nick = nick
        self.correo = correo
        self.num_actualizaciones = num_actualizaciones

    def __str__(self):
        return super().__str__() + f", num_actualizaciones: {self.num_actualizaciones}"