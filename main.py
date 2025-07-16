estudaintes={}
def RegistrarEstudiante():
    cantidad=int(input("Ingrese la cantidad de estudiantes seran registrados: "))
    for i in range(cantidad):
        print(f"\n Estudiante # {i+1}")
        carnet=int(input("Ingrese el carnet del estudiante: "))
        nombre=input("Ingrese el nombre del estudiante: ")
        edad=int(input("Ingrese la edad del estudiante: "))
        carrera=input("Ingrese la carrera del estudiante: ")
        cantidadCursos=int(input("Ingrese la cantidad de cursos que se le asignan al estudiante: "))
        for j in range(cantidadCursos):
            print(f"\n Cursos que se asignaran curso #{j+1}")
            codigocurso=input("Ingrese el codigo del curso: ")
            nombreCurso=input("Ingrese el nombre del curso: ")
            notadeTare=int(input("Ingrese la nota del estudiante: "))
            if 0<notadeTare > 100:
                print("La nota del estudiante no puede ser menor a 0 o mayor a 100 ")
            else:
                print("La nota se ha guardado correctamente: ")
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
              "codigocurso":{
                  "nombreCurso": nombreCurso,
                  "notaTare": notadeTare,
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
        print(f"Nombre del curso: {datos['codigocurso']}")
        print(f"Nombre del curso asignado: {datos['codigocurso']['nombreCurso']}")
        print(f"Nota de tarea: {datos['codigocurso']['notadeTare']}")
        print(f"Nota de Parcial: {datos['codigocurso']['notaParcial']}")
        print(f"Nota de Proyecto: {datos['codigocurso']['notaProyecto']}")

    print("\n Calculo de promedio")
    promedio=0
    if carnet in estudaintes:
        promedio= (estudaintes[carnet]['notadeTare']+estudaintes[carnet]['notaParcial']+estudaintes[carnet]['notaProyecto'])/3
    print(f"El promedio del estudiante es: {promedio}")

def BuscarPorCanet():
    print("\n Busqueda por medio de Carnet")
    buscado=int(input("Ingrese el numero de estudiante que desea buscar: "))
    if buscado in estudaintes:
       estudainte =estudaintes[buscado]
       print("\n Estudiante Encotrado")
       print(f"Nombre: {estudainte['nombre']}")
       print(f"Edad:{estudainte['edad']}")
       print(f"Carrera: {estudainte['carrera']}")
       print(f"Nombre del curso: {estudainte['nombreCurso']['curso']}")
       print(f"Nota de la tarea: {estudainte['nombreCurso']['notadeTare']}")
       print(f"Nota de Parcial: {estudainte['nombreCurso']['notaParcial']}")
       print(f"Nota de Proyecto: {estudainte['nombreCurso']['notaProyecto']}")
    else:
        print(f"EL {buscado} no existe en este registro")

def Menu():
    while True:
     print("\n ==Menu Principal==")
     print("1. Registrar Estudiante")
     print("2. Mostrar Informacion del Estudiante")
     print("3. Buscar Estudiante")
     print("4. Salir")
     opcion=int(input("Seleccione una opcion: "))
     if opcion==1:
        RegistrarEstudiante()
     elif opcion==2:
        MostrarEstudiantes()
     elif opcion==3:
         BuscarPorCanet()
     elif opcion==4:
         print("Fin del programa")
         break
     else:
         print("La opcion seleccionada no se encuetra disponible")


Menu()