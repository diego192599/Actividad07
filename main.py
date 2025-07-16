estudaintes={}
def RegistrarEstudiante():
    cantidad=int(input("Ingrese la cantidad de estudiantes seran registrados: "))
    for i in range(cantidad):
        print(f"\n Estudiante # {i+1}")
        carnet=int(input("Ingrese el carnet del estudiante: "))
        nombre=input("Ingrese el nombre del estudiante: ")
        edad=int(input("Ingrese la edad del estudiante: "))
        carrera=input("Ingrese la carrera del estudiante: ")
        cantidadCursos=int(input("Ingrese la cantidad de cursos que se le asignan al estudiante"))
        for i in range(cantidadCursos):
            print(f"\n Cursos que se asignaran curso #{i+1}")
            nombreCurso=input("Ingrese el nombre del curso")
            notadeTare=int(input("Ingrese la nota del estudiante: "))
            if 0<notadeTare > 100:
                print("La nota del estudiante no puede ser menor a 0 o mayor a 100 ")
            else:
                print("La nota se ha guardado correctamente")
            notaParcial=int(input("Ingrese la nota del parcial de estudiante: "))
            if 0<notaParcial >100:
                print("La nota del estudiante no puede ser menor a 0 o mayor a 100")
            else:
                print("La nota del parcial se ha guardado correctamente")
            notaProyecto=int(input("Ingrese la nota del proyecto: "))
            if 0< notaProyecto>100:
                print("La nota del proyecto no puede ser menor a 0 o mayor a 100")
            else:
                print("Se ha guardado correctamente la nota del proyecto")

        estudaintes[carnet]={
            "nombre": nombre,
             "edad": edad,
             "carrera": carrera,
              "nombreCursos":{
                  "notadeTarea":notadeTare,
                  "notaParcial":notaParcial,
                  "notaProyecto":notaProyecto
              }
        }

def MostrarEstudiantes():
    print("\n Lista de estudiantes")
    for carnet,datos in estudaintes.items():
        print(f"\n Carnet: {carnet}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Edad: {datos['edad']}")
        print(f"Carrera: {datos['carrera']}")
        print(f"Nombre del curso: {datos['nombreCurso']}")
        print(f"Nota de tarea: {datos['nombreCurso']['notadeTare']}")
        print(f"Nota de Parcial: {datos['nombreCurso']['notaParcial']}")
        print(f"Nota de Proyecto: {datos['nombreCurso']['notaProyecto']}")
