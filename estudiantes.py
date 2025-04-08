estudiantes={
      "Juan Perez":{"edad": 17, "materias":["Matematicas","Fisica"]},
      "Ana Gomez":{"edad":16, "materias":["Quimicas","Historia"]},
      "Pedro Lopez":{"edad":18,"materias":["Biologia","Ingles"]}
}

def agregar_estudiante():
    nombre=input("nombre del estudiante:")
    edad=int(input("edad del estudiante:"))
    materias=input("materias aprobadas(separadas por coma):").split(",")
    materias=[m.strip() for m in materias]
    estudiantes[nombre]={"edad": edad, "materias":materias}
    print("estudiante agregado.")

def mostrar_estudiantes():
    for nombre, info in estudiantes.items():
        print(f"nombre:{nombre}, edad:{info["edad"]},materias:{(info["materias"])}")

def eliminar_estudiante():
    nombre=input("nombre del estudiante a eliminar:")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print("estudiante eliminado.")
    else 
        print("estudiante no encontrado.")

def buscar_estudiante():
    nombre=input("nombre del estudiante a buscar:")
    if nombre in estudiantes:
        info=estudiantes[nombre]
        print=(f"nombre:{nombre}, edad:{info["edad"]},materias:{","["materias"]}")
    else
        print("estudiante no encontrado.")

def verificar_palabra():
    palabra = input ("palabra clabe a buscar en nombres: ")
    encontrados = [nombre for nombre in estudiantes if palabra.lower() in nombre.lower]
    if encontrados:
        print ("estudiantes que contienen la palabra clave en su nombre:")
        for nombre in encontrados:
            print (nombre)
    
    else:
        print("no se encontro ningun estudiante con esa palabra clave.")

def menu():
    while True:
        print("menu")
        print("1.agregar estudiante")
        print("2.mostrar estudiantes")
        print("3.eliminar estudiante")
        print("4.buscar estudiante")
        print("5.verificar palabra clave")
        print("6.salir")

        opcion=input("elige una opcion:")
        match opcion:
            case "1":
                agregar_estudiante()
            case "2":
                 mostrar_estudiantes()
            case "3":
                 eliminar_estudiate()
            case "4"
                buscar_estudiante()
            case "5"
                verificar_palabra()
            case "6"
                 print("programa finalizado")
                 break
            case_:
                 print("opcion invalida.intenta de nuevo")
                 

   