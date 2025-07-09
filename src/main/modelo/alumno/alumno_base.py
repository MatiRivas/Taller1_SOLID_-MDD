from abc import ABC, abstractmethod

class Alumno(ABC):
    
    def __init__(self, nombre, edad, rut, fecha_nacimiento, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
    
    def mostrar_info(self):
        
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"RUT: {self.rut}")
        print(f"Curso: {self.curso}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        
    @abstractmethod
    def get_tipo_alumno(self):
        pass
    
    

