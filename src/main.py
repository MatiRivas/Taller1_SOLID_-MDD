from main.modelo.alumno.tipos.alumno_titulado import AlumnoTitulado
from main.modelo.alumno.tipos.alumno_no_ayudante import AlumnoNoAyudante
from main.modelo.alumno.tipos.alumno_ayudante import AlumnoAyudante
from main.modelo.alumno.tipos.alumno_magister import AlumnoMagister
from main.modelo.alumno.tipos.alumno_doctorado import AlumnoDoctorado
from main.modelo.asignatura.asignatura import Asignatura
from main.modelo.gestor.gestor_alumnos import GestorAlumnos
from main.modelo.gestor.gestor_asignaturas import GestorAsignaturas

def main():
    # Crear gestores
    gestor_alumnos = GestorAlumnos()
    gestor_asignaturas = GestorAsignaturas()
    
    # Crear asignaturas
    asig1 = Asignatura("Programación", "PROG101", 4)
    asig2 = Asignatura("Matemáticas", "MATE101", 5)
    asig3 = Asignatura("Bases de Datos", "BD201", 3)
    
    gestor_asignaturas.crear_asignatura(asig1)
    gestor_asignaturas.crear_asignatura(asig2)
    gestor_asignaturas.crear_asignatura(asig3)
    
    # Crear diferentes tipos de alumnos
    alumno1 = AlumnoTitulado("Juan Pérez", 25, "12345678-9", "1999-01-15", "Ingeniero Civil")
    alumno2 = AlumnoNoAyudante("María García", 20, "98765432-1", "2004-03-20", "2do año", "Informática")
    alumno3 = AlumnoAyudante("Carlos López", 22, "11111111-1", "2002-07-10", "4to año", "Programación", "Ingeniería de Sistemas")
    alumno4 = AlumnoMagister("Ana Martínez", 26, "22222222-2", "1998-11-05", "Magíster", "Informatica")
    alumno5 = AlumnoDoctorado("Roberto Silva", 28, "33333333-3", "1996-09-12", "Doctorado")
    
    # Agregar alumnos al gestor
    gestor_alumnos.crear_alumno(alumno1)
    gestor_alumnos.crear_alumno(alumno2)
    gestor_alumnos.crear_alumno(alumno3)
    gestor_alumnos.crear_alumno(alumno4)
    gestor_alumnos.crear_alumno(alumno5)
    
    
    print("\n")
    print("DEMOSTRACIÓN DE OPERACIONES CRUD - GESTOR DE ALUMNOS")

    
    # 1. CREAR ALUMNOS
    print("\n1. CREAR ALUMNOS:")
    print(f"Total alumnos antes de crear: {len(gestor_alumnos.alumnos)}")
    
    # 2. RECUPERAR ALUMNO
    print("\n2. RECUPERAR ALUMNO POR RUT:")
    alumno_recuperado = gestor_alumnos.recuperar_alumno("12345678-9")
    if alumno_recuperado:
        print(f"Alumno encontrado: {alumno_recuperado.nombre} - {alumno_recuperado.get_tipo_alumno()}")
    else:
        print("Alumno no encontrado")
    
    # Intentar recuperar alumno que no existe
    alumno_no_existe = gestor_alumnos.recuperar_alumno("99999999-9")
    if alumno_no_existe:
        print(f"Alumno encontrado: {alumno_no_existe.nombre}")
    else:
        print("RUT 99999999-9: Alumno no encontrado (correcto)")
    
    # 3. MODIFICAR ALUMNO
    print("\n3. MODIFICAR ALUMNO:")
    alumno_original = gestor_alumnos.recuperar_alumno("98765432-1")
    if alumno_original:
        print(f"Antes: {alumno_original.nombre} - Edad: {alumno_original.edad}")
        
        # Crear una nueva versión del alumno con datos modificados
        alumno_modificado = AlumnoNoAyudante("María García López", 21, "98765432-1", "2004-03-20", "3er año", "Informática")
        exito_modificacion = gestor_alumnos.modificar_alumno("98765432-1", alumno_modificado)
        
        if exito_modificacion:
            alumno_actualizado = gestor_alumnos.recuperar_alumno("98765432-1")
            print(f"Después: {alumno_actualizado.nombre} - Edad: {alumno_actualizado.edad}")
        else:
            print("Error al modificar alumno")
    
    # 4. ELIMINAR ALUMNO
    print("\n4. ELIMINAR ALUMNO:")
    print(f"Total antes de eliminar: {len(gestor_alumnos.alumnos)}")
    alumno_a_eliminar = gestor_alumnos.recuperar_alumno("33333333-3")  # Roberto Silva
    if alumno_a_eliminar:
        print(f"   Eliminando: {alumno_a_eliminar.nombre}")
    
    exito_eliminacion = gestor_alumnos.eliminar_alumno("33333333-3")
    if exito_eliminacion:
        print("Alumno eliminado exitosamente")
    else:
        print("Error al eliminar alumno")
    print(f"Total después de eliminar: {len(gestor_alumnos.alumnos)}")
    
    print("\n")
    print("DEMOSTRACIÓN DE OPERACIONES CRUD - GESTOR DE ASIGNATURAS")
    
    # 1. CREAR ASIGNATURAS
    print("\n1. CREAR ASIGNATURAS:")
    print(f"Total asignaturas antes: {len(gestor_asignaturas.asignaturas)}")
    
    # Agregar más asignaturas para la demostración
    asig4 = Asignatura("Algoritmos", "ALG301", 4)
    asig5 = Asignatura("Redes", "RED401", 3)
    
    exito_asig4 = gestor_asignaturas.crear_asignatura(asig4)
    exito_asig5 = gestor_asignaturas.crear_asignatura(asig5)
    
    if exito_asig4:
        print("Asignatura Algoritmos creada")
    if exito_asig5:
        print("Asignatura Redes creada")
    
    print(f"Total asignaturas después: {len(gestor_asignaturas.asignaturas)}")
    
    # 2. RECUPERAR ASIGNATURA
    print("\n2. RECUPERAR ASIGNATURA POR CÓDIGO:")
    asignatura_recuperada = gestor_asignaturas.recuperar_asignatura("PROG101")
    if asignatura_recuperada:
        print(f"Asignatura encontrada: {asignatura_recuperada}")
    else:
        print("Asignatura no encontrada")
    
    # Intentar recuperar asignatura que no existe
    asig_no_existe = gestor_asignaturas.recuperar_asignatura("NOEXISTE")
    if asig_no_existe:
        print(f"Asignatura encontrada: {asig_no_existe}")
    else:
        print("Código NOEXISTE: Asignatura no encontrada (correcto)")
    
    # 3. MODIFICAR ASIGNATURA
    print("\n3. MODIFICAR ASIGNATURA:")
    asignatura_original = gestor_asignaturas.recuperar_asignatura("MATE101")
    if asignatura_original:
        print(f"Antes: {asignatura_original}")
        
        # Crear una nueva versión de la asignatura con datos modificados
        asignatura_modificada = Asignatura("Matemáticas Avanzadas", "MATE101", 6)
        exito_mod_asig = gestor_asignaturas.modificar_asignatura("MATE101", asignatura_modificada)
        
        if exito_mod_asig:
            asig_actualizada = gestor_asignaturas.recuperar_asignatura("MATE101")
            print(f"Después: {asig_actualizada}")
        else:
            print("Error al modificar asignatura")
    
    # 4. ELIMINAR ASIGNATURA
    print("\n4. ELIMINAR ASIGNATURA:")
    print(f"Total antes de eliminar: {len(gestor_asignaturas.asignaturas)}")
    asignatura_a_eliminar = gestor_asignaturas.recuperar_asignatura("RED401")
    if asignatura_a_eliminar:
        print(f"Eliminando: {asignatura_a_eliminar.nombre}")
    
    exito_elim_asig = gestor_asignaturas.eliminar_asignatura("RED401")
    if exito_elim_asig:
        print("Asignatura eliminada exitosamente")
    else:
        print("Error al eliminar asignatura")
    print(f"Total después de eliminar: {len(gestor_asignaturas.asignaturas)}")
    
    # Obtener alumnos restantes después de las operaciones CRUD
    alumno1_actual = gestor_alumnos.recuperar_alumno("12345678-9")
    alumno2_actual = gestor_alumnos.recuperar_alumno("98765432-1")
    alumno3_actual = gestor_alumnos.recuperar_alumno("11111111-1")
    alumno4_actual = gestor_alumnos.recuperar_alumno("22222222-2")

    
    alumnos_actuales = [alumno1_actual, alumno2_actual, alumno3_actual, alumno4_actual]
    
    for alumno in alumnos_actuales:
        if alumno:
            print(f"\n{alumno.nombre} ({alumno.get_tipo_alumno()}):")
            alumno.mostrar_info()
            
            # Demostrar comportamientos específicos
            if hasattr(alumno, 'estudiar'):
                alumno.estudiar()
                if hasattr(alumno, 'descargar_notas'):
                    alumno.descargar_notas()
            
            if isinstance(alumno, AlumnoTitulado):
                alumno.mostrar_titulo()
            elif isinstance(alumno, AlumnoAyudante):
                alumno.hacer_ayudantias()
                alumno.estudiar()
            elif isinstance(alumno, AlumnoMagister):
                alumno.estudiar()
                alumno.hacer_clases()
    
    # Demostración específica de ISP (Interface Segregation Principle)
    print("\n")
    print("DEMOSTRACIÓN ISP: ¿QUIÉN PUEDE DESCARGAR NOTAS?")
    
    for alumno in alumnos_actuales:
        if alumno:
            print(f"\n{alumno.nombre} ({alumno.get_tipo_alumno()}):")
            if hasattr(alumno, 'descargar_notas'):
                print("SÍ puede descargar notas")
                alumno.descargar_notas()
            else:
                print("NO puede descargar notas")
                print("   Razón: Los titulados ya completaron sus estudios")

    
    print("\n")
    print("RESUMEN FINAL DEL SISTEMA")

    print(f"Total de alumnos registrados: {len(gestor_alumnos.alumnos)}")
    print(f"Total de asignaturas registradas: {len(gestor_asignaturas.asignaturas)}")
    
    print("\nAsignaturas disponibles:")
    for asignatura in gestor_asignaturas.asignaturas:
        print(f"   - {asignatura}")
    
    print("\nAlumnos registrados:")
    for alumno in gestor_alumnos.alumnos:
        print(f"   - {alumno.nombre} ({alumno.get_tipo_alumno()}) - RUT: {alumno.rut}")

if __name__ == "__main__":
    main()
