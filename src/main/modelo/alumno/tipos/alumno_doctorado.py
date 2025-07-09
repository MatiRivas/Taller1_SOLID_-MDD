from ..alumno_que_estudia import AlumnoQueEstudia

class AlumnoDoctorado(AlumnoQueEstudia):
    
    def __init__(self, nombre, edad, rut, fecha_nacimiento, curso):
        super().__init__(nombre, edad, rut, fecha_nacimiento, curso)
    
    def get_tipo_alumno(self):
        return "Doctorado"
    
    def estudiar(self):
        print("Estoy estudiando e investigando para mi doctorado")
    
    def hacer_clases(self):
        print("haciendo clases")
    
    def investigar(self):
        print("Estoy investigando")
    