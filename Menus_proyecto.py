import Funciones_listas
#Definimos el Menú principal en un bucle oreventivo a opciones erroneas

def menu_principal():
    while True:
        print("\n")
        print("Menú principal:\n1. Empleados\n2. Clientes\n3. Trabajos\n4. Salir")
        opcion= input("Ingrese una opción: ")
        if opcion == "1":
            menu_empleados()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_trabajos()
        elif opcion == "4":
                break
        else:
            print(f"{opcion} no es una opción válida, intente otra vez\n")
            continue

#Ahora el menú de empleados, usando el mismo esquema

def menu_empleados():
    while True:
        print("\n")
        print("Menú de empleados:\n1. Ingresar empleado\n2. Borrar empleado\n3. Ver empleados\n4. Salir")
        opcion= input("Ingrese una opción: ")
        if opcion == "1":
            Funciones_listas.ingresar_empleado()
        elif opcion == "2":
            Funciones_listas.borrar_empleado()
        elif opcion == "3":
            Funciones_listas.ver_empleados()
        elif opcion == "4":
                break
        else:
            print(f"{opcion} no es una opción válida, intente otra vez\n")
            continue

#Menú de clientes

def menu_clientes():
    while True:
        print("\n")
        print("Menú de cliente:\n1. Ingresar cliente\n2. Modificar cliente\n3. Ver cliente\n4. Salir")
        opcion= input("Ingrese una opción: ")
        if opcion == "1":
            Funciones_listas.ingresar_cliente()
        elif opcion == "2":
            Funciones_listas.modificar_cliente()
        elif opcion == "3":
            Funciones_listas.ver_cliente()
        elif opcion == "4":
                break
        else:
            print(f"{opcion} no es una opción válida, intente otra vez\n")
            continue

#Menú de trabajos

def menu_trabajos():
    while True:
        print("\n")
        print("Menú de trabajos:\n1. Brindar servicio\n2. Ver servicios brindados\n3. Empleado disponible\n4. Salir")
        opcion= input("Ingrese una opción: ")
        if opcion == "1":
            Funciones_listas.brindar_servicio()
        elif opcion == "2":
            Funciones_listas.ver_servicios_brindados()
        elif opcion == "3":
            Funciones_listas.ver_empleados_disponibles()
        elif opcion == "4":
                break
        else:
            print(f"{opcion} no es una opción válida, intente otra vez\n")
            continue