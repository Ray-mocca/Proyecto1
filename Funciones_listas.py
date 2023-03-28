#-------------------------------------Empleados----------------------------------

empleados = []
clientes = []
trabajos = []

def ingresar_empleado():
    nombre = input("Ingrese nombre del empleado: ")
    especialidad = input("Ingrese especialidad del empleado: ")
    sexo = input("Ingrese sexo del empleado: ")

    empleado = {
        "nombre": nombre,
        "especialidad": especialidad,
        "sexo": sexo
    }

    empleados.append(empleado)
    print("Empleado ingresado exitosamente\n")

def borrar_empleado():
    nombre = input("Ingrese nombre del empleado a borrar: ")
    
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            empleados.remove(empleado)
            print("Empleado borrado exitosamente.\n")
            return
        else:
            print("No se encontró el empleado especificado.\n")

def ver_empleados():
    if len(empleados) == 0:
        print("No hay empleados ingresados.\n")
    else:
        for empleado in empleados:
            print(f"Nombre: {empleado['nombre']}")
            print(f"Especialidad: {empleado['especialidad']}")
            print(f"Sexo: {empleado['sexo']}")
            print("\n")

#-------------------------------------Clientes----------------------------------

def ingresar_cliente():
    nombre = input("Ingrese nombre del cliente: ")
    cedula = input("Ingrese cédula del cliente: ")
    telefono = input("Ingrese teléfono del cliente: ")

    cliente = {
        "nombre": nombre,
        "cedula": cedula,
        "telefono": telefono
    }
    clientes.append(cliente)
    print("Cliente ingresado exitosamente\n")

def modificar_cliente():
    cedula = input("Ingrese cédula del cliente a modificar: ")
    
    for cliente in clientes:
        if cliente["cedula"] == cedula:
            print(f"El cliente actual es:")
            print(f"Nombre: {cliente['nombre']}")
            print(f"cedula: {cliente['cedula']}")
            print(f"telefono: {cliente['telefono']}")
            print("\n")
            nombre = input("Ingrese el nuevo nombre del cliente: ")
            telefono = input("Ingrese el nuevo teléfono del cliente: ")
            cliente["nombre"] = nombre
            cliente["telefono"] = telefono
            print("Cliente modificado exitosamente.")
            return
        else:
            print("No se encontró el cliente especificado.")

def ver_cliente():
    if len(clientes) == 0:
        print("No hay clientes ingresados.")
    else:
        cedula = input("Ingrese cédula del cliente que desea ver: ")
        
        for cliente in clientes:
            if cliente["cedula"] == cedula:
                print(f"Nombre: {cliente['nombre']}")
                print(f"Cédula: {cliente['cedula']}")
                print(f"Teléfono: {cliente['telefono']}")
                return
            else:
                print("No se encontró el cliente especificado.")

#-------------------------------------Trabajos----------------------------------

def brindar_servicio():
    #Debemos verificar que hayan clientes y empleados
    if not empleados:
        print("No hay empleados registrados.")
        return
    if not clientes:
        print("No hay clientes registrados.")
        return
    
    #Obtenemos los datos del cliente
    cedula = input("Ingrese la cédula del cliente: ")
    cliente = None
    for c in clientes:
        if c['cedula'] == cedula:
            cliente = c
            break
    if not cliente:
        print("No se encontró el cliente.")
        return
    
    #Obtenemos los datos del servicio y del empleado
    servicio = input("Ingrese el tipo de servicio: ")
    especialidad = input("Ingrese la especialidad que necesita(técnico, mecánico, plomero, electricista, etc): ")
    empleados_disponibles = [e for e in empleados if e['especialidad'] == especialidad]
    if not empleados_disponibles:
        print("No hay empleados disponibles con la especialidad requerida.\n")
        return
    print("\n")
    print("Empleados disponibles:")
    for e in empleados_disponibles:
        print(f"{e['nombre']} - {e['especialidad']}")
        print("\n")
    empleado = None
    while not empleado:
        nombre_empleado = input("Ingrese el nombre del empleado a contratar: ")
        for e in empleados_disponibles:
            if e['nombre'] == nombre_empleado:
                empleado = e
                break
        if not empleado:
            print("El empleado ingresado no está disponible.")
    
    #Revisamos la fecha deseada
    fecha = input("Ingrese la fecha del trabajo (dd/mm/aaaa): ")
    
    #Registramos el trabajo
    trabajos.append({
        "fecha": fecha,
        "cliente": cliente["nombre"],
        "servicio": servicio,
        "empleado": empleado["nombre"]
    })
    
    print("Trabajo registrado exitosamente.")

def ver_servicios_brindados():
    if not trabajos:
        print("No hay trabajos registrados.\n")
        return
    print("Trabajos registrados: ")
    for trabajo in trabajos:
        print("- Fecha:", trabajo["fecha"])
        print("  Cliente:", trabajo["cliente"])
        print("  Servicio:", trabajo["servicio"])
        print("  Empleado:", trabajo["empleado"])

def ver_empleados_disponibles():
    especialidad = input("Ingrese la especialidad que busca: ")
    disponibles = [empleado["nombre"] for empleado in empleados if empleado["especialidad"] == especialidad]

    if not disponibles:
        print("No hay empleados disponibles con la especialidad requerida.")
        return
    
    print("Empleados disponibles:")
    for empleado in disponibles:
        print("- " + empleado)