class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} tiene {self.edad} años"
    
persona1 = Persona("Juan", "Pérez", 30)
persona2 = Persona("Pedro", "Pérez", 30)

print(persona1, persona2, sep="\n")