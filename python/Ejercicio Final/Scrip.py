# Desarrollar un programa controlado por menú de opciones, que permita realizar en forma completa
# la gestión de un archivo de registros de automoviles de una concesionaria. Por cada auto, prevea
# tres campos para la patente, el estado (0-vendido, 1-disponible) y el modelo (que es el año de fabricación).
#
# El programa debe incluir opciones que permitan:
#
# Realizar altas de registros en el archivo.
# Realizar ventas de un automóvil con patente x, ingresada por teclado.
# Mostrar el contenido completo del archivo.
# Mostrar los datos de los autos disponibles con modelo mayor m, ingresado por teclado.


from  auto import *
import io
import os
import pickle
import os.path
def clear():
    os.system("cls")
    

def buscar(fd, m, p):   
    t = os.path.getsize(fd)

    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)

    posicion = -1
    while m.tell() < t:
        fp = m.tell()
        aut = pickle.load(m)
        if aut.patente == p:
            posicion = fp
            break

    m.seek(fp_inicial, io.SEEK_SET)
    return posicion

# punto 1

def alta(fd):
    
    m = open(fd, 'a+b')

    patente = input('Patente del auto a registrar (cargue 0 para salir): ')
    while patente != '0':
        
        pos = buscar(fd, m, patente)

        if pos == -1:
            
            modelo = int(input('Modelo: '))
            aut = Auto(patente, modelo)
            pickle.dump(aut, m)
            m.flush()
            print('Registro grabado en el archivo...')

        else:
            print('Patente repetida... alta rechazada...')

        patente = input('Otra patente (cargue 0 para salir): ')

    print()
    print('Los nuevos registros han sido grabados...')
    input('Presione  para seguir...')
    m.close()
           
   
# punto 2


def modificacion(fd):
    
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    m = open(fd, 'r+b')

    patente = input('Patente del automovil a modificar su estado (cargue 0 para salir): ')
    while patente != 'vendido':
        # buscamos el registro con esa patente...
        pos = buscar(fd, m, patente)

        if pos != -1:
            # encontrado... procedemos a cargarlo...
            m.seek(pos, io.SEEK_SET)
            aut = pickle.load(m)

            # ...mostramos el registro tal como estaba...
            print()
            print('El registro actualmente grabado es:')
            to_string(aut)

            if aut.estado == 0:
                print('El automovil ya fue VENDIDO')
            else:
                aut.estado = 0
                m.seek(pos, io.SEEK_SET)
                pickle.dump(aut, m)
                print()
                print('El automovil cambio su estado a VENDIDO...')
        else:
            print('Ese registro no existe en el archivo...')

        input('Presione  para seguir...')
        patente = input('Otra patente a modificar su estado (cargue 0 para salir): ')
    m.close()           
# punto 3

def listado_completo(fd):
    
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    tbm = os.path.getsize(fd)

    m = open(fd, 'rb')

    print('Listado general de automoviles registrados:')
    while m.tell() < tbm:
        aut = pickle.load(m)
        to_string(aut)

    m.close()

    print()
    input('Presione  para seguir...')
                
 # punto 4

def listado_filtrado(fd):
    
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    tbm = os.path.getsize(fd)

    m = open(fd, 'rb')

    modelo = int(input('Modelo de automovil para filtrar: '))

    print('Listado de automoviles disponibles con modelo mayor a ' + str(modelo))
    while m.tell() < tbm:
        aut = pickle.load(m)
        if aut.estado == 1 and aut.modelo > modelo:
            to_string(aut)

    m.close()

    print()
    input('Presione  para seguir...')
# menu principal

def main():
    fd = 'automoviles.aut'

    op = 0
    while op != 5:
        
        print("/////////////// Bienvenido a nuestro Menu Automoviles ///////////////")
        print('*'  *80 )
        print('   1----> Alta de automoviles')
        print('   2----> Modificación de estado de un automovil')
        print('   3----> Listado completo de automoviles')
        print('   4----> Listado de automoviles disponibles con modelo mayor a m')
        print('   0----> Salir')
        print('*'  *80 )
        op = int(input('\t\tIngrese número de la opción elegida: '))
        print()
        
        if op == 1:
            alta(fd)

        elif op == 2:
            modificacion(fd)

        elif op == 3:
            listado_completo(fd)

        elif op == 4:
            listado_filtrado(fd)

        elif op == 0:
            print(" !!!!!Gracias por usar nuestro Sistema¡¡¡¡¡")
        else:
            print("Opcion incorrecta......")
            print("Elija Nuevamente otra opcion....")
            
clear()
# script principal...
if __name__ == '__main__':
    main()              
                

                

        

    




