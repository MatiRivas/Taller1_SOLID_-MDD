from ..alumno_que_estudia import AlumnoQueEstudia

class AlumnoNoAyudante(AlumnoQueEstudia):
    
    def __init__(self, nombre, edad, rut, fecha_nacimiento, curso, carrera):
        super().__init__(nombre, edad, rut, fecha_nacimiento, curso)
        self.carrera = carrera
    
    def get_tipo_alumno(self):
        return "No Ayudante"
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando normalmente")
    
    
