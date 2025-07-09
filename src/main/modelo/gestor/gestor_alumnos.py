from typing import List, Optional
from ..alumno.alumno_base import Alumno

class GestorAlumnos:

    def __init__(self):
        self.alumnos: List[Alumno] = []
    
    def crear_alumno(self, alumno: Alumno) -> bool:
        if isinstance(alumno, Alumno):
            # Verificar que no exista un alumno con el mismo RUT
            if not self.recuperar_alumno(alumno.rut):
                self.alumnos.append(alumno)
                return True
        return False
    
    def recuperar_alumno(self, rut: str):
        for alumno in self.alumnos:
            if alumno.rut == rut:
                return alumno
        return None
    
    def modificar_alumno(self, rut: str, nuevo_alumno: Alumno) -> bool:
        for i, alumno in enumerate(self.alumnos):
            if alumno.rut == rut:
                self.alumnos[i] = nuevo_alumno
                return True
        return False
    
    def eliminar_alumno(self, rut: str) -> bool:
        for i, alumno in enumerate(self.alumnos):
            if alumno.rut == rut:
                del self.alumnos[i]
                return True
        return False