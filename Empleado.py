class Empleado:
    def __init__(self, nick, correo):
        self.nick = nick
        self.correo = correo

    def __str__(self):
        return f"nick: {self.nick}, correo: {self.correo}"

