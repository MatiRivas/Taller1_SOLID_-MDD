from .alumno_base import Alumno

class AlumnoQueNoEstudia(Alumno):
    #Clase para alumnos que ya no estudian (titulados)
    
    def get_tipo_alumno(self):
        return "Alumno que no estudia"
    
    def actividad_principal(self):
        print("Ya completé mis estudios académicos")
