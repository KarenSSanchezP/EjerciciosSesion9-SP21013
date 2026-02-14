# Ejercicio 4
# Diseñar un programa que permita la creación de usuarios de 
# estudiantes y profesores, debemos considerar los atributos 
# de usuario o carnet, nombres, apellidos y facultad. Una vez 
# creado el objeto, almacenarlo en un archivo de texto o csv.

class Estudiante_Profesor():
    def __init__(self, rol, nombre, apellidos, facultad, usuario=None, carnet=None):
        self.rol = rol # Estudiante o Profesor
        self.nombre = nombre
        self.apellidos = apellidos
        self.facultad = facultad
        self.usuario = usuario if usuario else "N/A"
        self.carnet = carnet if carnet else "N/A"
    
    def __str__(self):
        return f"{self.rol.capitalize()}: {self.nombre} {self.apellidos}, Facultad: {self.facultad}, Usuario: {self.usuario}, Carnet: {self.carnet}"
        
    def a_csv(self):
        return f"{self.rol},{self.nombre},{self.apellidos},{self.facultad},{self.usuario},{self.carnet}"


def leer_archivo():
    file_path = "./estudiantes_profesores.txt"
    
    print("\n--- LISTADO DE USUARIOS ---")
    try:
        with open(file_path, 'r') as file:
            for linea in file:
                linea = linea.strip() # Eliminar espacios en blanco al inicio/final
                if linea:
                    rol, nombre, apellidos, facultad, usuario, carnet = linea.split(',')
                    
                    persona = Estudiante_Profesor(rol,nombre, apellidos, facultad, usuario, carnet)
                    print(persona)
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def guardar_en_archivo(persona):
    file_path = "./estudiantes_profesores.txt"
    try:
        with open(file_path, 'a') as file:
            file.write(persona.a_csv() + "\n")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def menu():
    while True:
        print("\nOpciones:")
        print("1. Crear un estudiante")
        print("2. Crear un profesor")
        print("3. Listar todos los usuarios")
        print("4. Salir")
        opcion = input("Opción: ")
        
        if opcion == "1" or opcion == "2":
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            facultad = input("Facultad: ")
            
            if opcion == "1":
                rol = "estudiante"
                carnet = input("Carnet: ")
                usuario = None
            else:
                rol = "profesor"
                usuario = input("Usuario: ")
                carnet = None
            
            nueva_persona = Estudiante_Profesor(rol, nombre, apellidos, facultad, usuario, carnet)            
            guardar_en_archivo(nueva_persona)
            print(f"Se ha creado el usuario exitosamente.")
            
        elif opcion == "3":
            leer_archivo()
            
        elif opcion == "4":
            print("Adiós!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()