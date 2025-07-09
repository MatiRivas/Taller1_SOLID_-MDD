class Asignatura:
    """
    Clase que representa una asignatura académica
    """
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
    
    def mostrar_info(self):
        print(f"Asignatura: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Créditos: {self.creditos}")
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre} ({self.creditos} créditos)"
    
    def __eq__(self, other):
        if isinstance(other, Asignatura):
            return self.codigo == other.codigo
        return False
