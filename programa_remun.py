from os import system
def menu_principal():
    opciones = {
        '1': ('Registrar Trabajadores', reg_trabajador),
        '2': ('Listar trabajadores', listar_trabajador),
        '3': ('Imprimir plantilla suledos', imprimir_trabajador),
        '4': ('Salir del programa', salir)
    }

    generar_menu(opciones, '4')

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        system("cls")
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave} {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def reg_trabajador():
    print('Has elegido la opción 1')
    input()


def listar_trabajador():
    print('Has elegido la opción 2')
    input()

def imprimir_trabajador():
    print('Has elegido la opción 3')
    input()

def salir():
    print('Saliendo')
    input()

menu_principal()