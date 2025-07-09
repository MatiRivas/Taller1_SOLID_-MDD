from ..alumno_que_estudia import AlumnoQueEstudia

class AlumnoMagister(AlumnoQueEstudia):

    def __init__(self, nombre, edad, rut, fecha_nacimiento, curso, carrera):
        super().__init__(nombre, edad, rut, fecha_nacimiento, curso)
        self.carrera = carrera
          
    
    def get_tipo_alumno(self):
        return "Magíster"
    
    def estudiar(self):
        print("Estoy estudiando materias avanzadas de magíster")
    
    def hacer_clases(self):
        print("Estoy haciendo clases")
    
    
