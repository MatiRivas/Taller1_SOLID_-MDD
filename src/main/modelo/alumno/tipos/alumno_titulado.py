from ..alumno_que_no_estudia import AlumnoQueNoEstudia

class AlumnoTitulado(AlumnoQueNoEstudia):
    
    def __init__(self, nombre, edad, rut, fecha_nacimiento, titulo_obtenido):
        super().__init__(nombre, edad, rut, fecha_nacimiento, curso=None)
        self.titulo_obtenido = titulo_obtenido
    
    def get_tipo_alumno(self):
        return "Titulado"
    
    def mostrar_titulo(self):
        print(f"Título obtenido: {self.titulo_obtenido}")
    
    def actividad_principal(self):
        print("Ya completé mis estudios y obtuve mi título")
        self.mostrar_titulo()
