from typing import List, Optional
from ..asignatura.asignatura import Asignatura

class GestorAsignaturas:
    def __init__(self):
        self.asignaturas: List[Asignatura] = []
    
    def crear_asignatura(self, asignatura: Asignatura) -> bool:
        if isinstance(asignatura, Asignatura):
            # Verificar que no exista una asignatura con el mismo código
            if not self.recuperar_asignatura(asignatura.codigo):
                self.asignaturas.append(asignatura)
                return True
        return False
    
    def recuperar_asignatura(self, codigo: str) -> Optional[Asignatura]:
        for asignatura in self.asignaturas:
            if asignatura.codigo == codigo:
                return asignatura
        return None
    
    def modificar_asignatura(self, codigo: str, nueva_asignatura: Asignatura) -> bool:
        for i, asignatura in enumerate(self.asignaturas):   
            if asignatura.codigo == codigo:
                self.asignaturas[i] = nueva_asignatura
                return True
        return False
    
    def eliminar_asignatura(self, codigo: str) -> bool:
        for i, asignatura in enumerate(self.asignaturas):
            if asignatura.codigo == codigo:
                del self.asignaturas[i]
                return True
        return False
    
