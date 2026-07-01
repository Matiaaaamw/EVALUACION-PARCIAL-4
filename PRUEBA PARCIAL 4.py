def mostrar_menu():
    print("========== MENU PRINCIPAL ==========")
    print("1. Agregar paciente")
    print("2. Buscar paciente")
    print("3. Eliminar paciente")
    print("4. Actualizar estado")
    print("5. Mostrar pacientes")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        try:
            op = int(input("Ingrese una opcion: "))
            if 1 <= op <= 6:
                return op
            print("Opcion invalida Debe ingresar un numero entre 1 y 6")
        except ValueError:
            print("Entrada invalida Ingrese un numero")


def validar_nombre(nombre):
    return bool(nombre and nombre.strip())


def validar_edad(edad_str):
    try:
        edad = int(edad_str)
        return edad > 0
    except Exception:
        return False


def validar_temperatura(temp_str):
    try:
        t = float(temp_str)
        return 35.0 <= t <= 42.0
    except Exception:
        return False


def agregar_paciente(lista):
    nombre = input("Nombre: ")
    edad_str = input("Edad: ")
    temp_str = input("Temperatura: ")

    ok_nombre = validar_nombre(nombre)
    ok_edad = validar_edad(edad_str)
    ok_temp = validar_temperatura(temp_str)

    if not ok_nombre:
        print("Error el nombre no puede estar vacio ni solo espacios en blanco")
        return
    if not ok_edad:
        print("Error la edad debe ser un numero entero mayor que cero")
        return
    if not ok_temp:
        print("Error la temperatura debe ser un numero entre 35.0 y 42.0")
        return

    paciente = {
        "nombre": nombre.strip(),
        "edad": int(edad_str),
        "temperatura": float(temp_str),
        "atendido": False,
    }
    lista.append(paciente)
    print("Paciente agregado correctamente")


def buscar_paciente(lista, nombre_buscar):
    for i, paciente in enumerate(lista):
        if paciente.get("nombre") == nombre_buscar:
            return i
    return -1


def eliminar_paciente(lista):
    nombre = input("Nombre del paciente a eliminar: ")
    pos = buscar_paciente(lista, nombre)
    if pos == -1:
        print(f"El paciente '{nombre}' no se encuentra registrado")
    else:
        lista.pop(pos)
        print("Paciente eliminado correctamente")


def actualizar_estado(lista):
    for paciente in lista:
        if paciente.get("temperatura", 0) <= 37.0:
            paciente["atendido"] = True
        else:
            paciente["atendido"] = False
    print("Estados actualizados")


def mostrar_pacientes(lista):
    actualizar_estado(lista)
    print("=== LISTA DE PACIENTES ===")
    if not lista:
        print("No hay pacientes registrados")
        return
    for paciente in lista:
        estado = "ATENDIDO" if paciente.get("atendido") else "REQUIERE ATENCION"
        print(f"Nombre: {paciente.get('nombre')}")
        print(f"Edad: {paciente.get('edad')}")
        print(f"Temperatura: {paciente.get('temperatura')}")
        print(f"Estado: {estado}")
        print("********************************************")


def main():
    pacientes = []
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            agregar_paciente(pacientes)
        elif opcion == 2:
            nombre = input("Nombre a buscar: ")
            pos = buscar_paciente(pacientes, nombre)
            if pos == -1:


if __name__ == '__main__':
    main()
