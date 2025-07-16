estudiantes = {}


def RegistrarEstudiante():
    cantidad = int(input("Ingrese la cantidad de estudiantes que serán registrados: "))
    for i in range(cantidad):
        print(f"\nEstudiante #{i + 1}")
        carnet = int(input("Ingrese el carnet del estudiante: "))
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        carrera = input("Ingrese la carrera del estudiante: ")

        print("\nDatos del curso asignado")
        codigo_curso = input("Ingrese el código del curso: ")
        nombre_curso = input("Ingrese el nombre del curso: ")

        while True:
            nota_tarea = int(input("Ingrese la nota de la tarea: "))
            if 0 <= nota_tarea <= 100:
                break
            print("La nota debe estar entre 0 y 100.")

        while True:
            nota_parcial = int(input("Ingrese la nota del parcial: "))
            if 0 <= nota_parcial <= 100:
                break
            print("La nota debe estar entre 0 y 100.")

        while True:
            nota_proyecto = int(input("Ingrese la nota del proyecto: "))
            if 0 <= nota_proyecto <= 100:
                break
            print("La nota debe estar entre 0 y 100.")

        estudiantes[carnet] = {
            "nombre": nombre,
            "edad": edad,
            "carrera": carrera,
            "curso": {
                "codigo": codigo_curso,
                "nombre": nombre_curso,
                "notaTarea": nota_tarea,
                "notaParcial": nota_parcial,
                "notaProyecto": nota_proyecto
            }
        }


def MostrarEstudiantes():
    print("\nLista de estudiantes registrados:")
    for carnet, datos in estudiantes.items():
        print(f"\nCarnet: {carnet}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Edad: {datos['edad']}")
        print(f"Carrera: {datos['carrera']}")
        print(f"Curso asignado: {datos['curso']['nombre']} ({datos['curso']['codigo']})")
        print(f"Nota de tarea: {datos['curso']['notaTarea']}")
        print(f"Nota de parcial: {datos['curso']['notaParcial']}")
        print(f"Nota de proyecto: {datos['curso']['notaProyecto']}")
        promedio = (datos['curso']['notaTarea'] + datos['curso']['notaParcial'] + datos['curso']['notaProyecto']) / 3
        print(f"Promedio: {promedio:.2f}")


def BuscarPorCarnet():
    print("\nBúsqueda por carnet:")
    buscado = int(input("Ingrese el número de carnet: "))
    if buscado in estudiantes:
        est = estudiantes[buscado]
        print(f"\nEstudiante encontrado:")
        print(f"Nombre: {est['nombre']}")
        print(f"Edad: {est['edad']}")
        print(f"Carrera: {est['carrera']}")
        print(f"Curso: {est['curso']['nombre']} ({est['curso']['codigo']})")
        print(f"Nota de tarea: {est['curso']['notaTarea']}")
        print(f"Nota de parcial: {est['curso']['notaParcial']}")
        print(f"Nota de proyecto: {est['curso']['notaProyecto']}")
        promedio = (est['curso']['notaTarea'] + est['curso']['notaParcial'] + est['curso']['notaProyecto']) / 3
        print(f"Promedio: {promedio:.2f}")
    else:
        print("Carnet no encontrado.")


def Menu():
    while True:
        print("\n== Menú Principal ==")
        print("1. Registrar Estudiante")
        print("2. Mostrar Información de Estudiantes")
        print("3. Buscar Estudiante por Carnet")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            RegistrarEstudiante()
        elif opcion == 2:
            MostrarEstudiantes()
        elif opcion == 3:
            BuscarPorCarnet()
        elif opcion == 4:
            print("Fin del programa.")
            break
        else:
            print("Opción no válida.")


Menu()
