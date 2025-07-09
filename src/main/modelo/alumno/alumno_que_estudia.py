from abc import abstractmethod
from .alumno_base import Alumno

class AlumnoQueEstudia(Alumno):

    
    @abstractmethod
    def estudiar(self):
        pass

    def descargar_notas(self):
        print(f"{self.nombre} está descargando las notas del aula virtual de sus asignaturas.")