from datetime import datetime

class log:

    #

    def escribir_fichero(self, evento, info):
        fechaActual = datetime.now()
        archivo = "log/" + fechaActual.strftime("%d-%m-%Y-call.log")
        with open("29-11-2024airEuropa.log.txt", "a") as f:
            f.write(archivo + " " + evento + " " +  info + "\r")
            #

