from ..alumno_que_estudia import AlumnoQueEstudia

class AlumnoAyudante(AlumnoQueEstudia):
    
    def __init__(self, nombre, edad, rut, fecha_nacimiento, curso, asignatura_ayudantia, carrera):
        super().__init__(nombre, edad, rut, fecha_nacimiento, curso)
        self.asignatura_ayudantia = asignatura_ayudantia
        self.carrera = carrera
    
    def get_tipo_alumno(self):
        return "Ayudante"
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando y también hace ayudantías")
    
    def hacer_ayudantias(self):
        print(f"Realizando ayudantía en {self.asignatura_ayudantia}")
    
    