# Clase Date que representa una fecha con día, mes y año.
class Date():
    def __init__(self, day, month,year):
        self.day = day
        self.month = month
        self.year = year

    def formatear(self, numero, cifras):
        numero = str(numero)
        ceros_faltantes = "0" * (cifras - len(numero))
        return f"{ceros_faltantes}{numero}"
    
    def __str__(self):
        return "{}/{}/{}".format(self.formatear(self.day, 2), 
                                self.formatear(self.month, 2), 
                                self.formatear(self.year, 4))

# Prueba de la clase Date
fecha1 = Date(15,7,4)
fecha2 = Date(1,1,24)
fecha3 = Date(25,12,224)
fecha4 = Date(2,9,2000)
print(fecha1, fecha2, fecha3, fecha4, sep="\n")
