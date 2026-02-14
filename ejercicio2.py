class Estudiante():
    def __init__(self, carnet, nombre, apellidos, carrera):
        self.carnet = carnet
        self.nombre = nombre
        self.apellidos = apellidos
        self.carrera = carrera

# Ruta del archivo de estudiantes
file_path = "./estudiantes_practica.txt"

lista_estudiantes = []

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        # Saltar la primera línea si es un encabezado
        next(file)
        for line in file:
            line = line.strip() # Eliminar espacios en blanco al inicio/final
            if line:
                try:
                    carnet, nombre, apellidos, carrera = line.split(',')

                    # Crear una nueva instancia de Persona
                    estudiante = Estudiante(carnet, nombre, apellidos, carrera)
                    lista_estudiantes.append(estudiante)
                except ValueError as e:
                    print(f"Error al procesar la línea '{line}': {e}. Asegúrate de que el formato sea 'nombre,apellidos,edad'.")

    print(f"Se han cargado {len(lista_estudiantes)} estudiantes.")
    # Puedes imprimir los estudiantes cargados para verificar
    for est in lista_estudiantes:
        print(f"Carnet: {est.carnet} Nombre: {est.nombre}, Apellidos: {est.apellidos}, Edad: {est.carrera}")

except FileNotFoundError:
    print(f"Error: El archivo '{file_path}' no fue encontrado. Por favor, verifica la ruta y asegúrate de que el archivo exista.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")