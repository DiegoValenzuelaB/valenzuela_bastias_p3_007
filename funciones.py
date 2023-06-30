import numpy as np
import os
import msvcrt

guarderia=np.zeros((2,5),int)
vdia=15000
lista_ruts=[]
lista_nombres=[]
lista_nom_masc=[]
lista_identificador=[]
lista_dias=[]
lista_pisos=[1,2]
lista_sala=[1,2,3,4,5]

def salida():
    print("USTED HA SALIDO DEL PROGRAMA!")

def menu():
    os.system('cls')
    print("""
    
    MENÚ:
    1. GRABAR 
    2. BUSCAR 
    3. RETIRARSE 
    4. SALIR
    """)

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")

def validar_rut():
    os.system('cls')
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! RUT ENTRE 1000000 Y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    os.system('cls')
    while True:
        nom = input("Ingrese nombre: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")

def validar_nombre_masc():
    os.system('cls')
    while True:
        nom = input("Ingrese nombre de mascota: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")

def ver_guarderia():
    os.system('cls')
    print("GUARDERIA:")

    print("          1 2 3 4 5")
    for x in range(2):
        print("Piso", lista_pisos[x],'->' ,end=" ")
        for y in range(5):
            print(guarderia[x][y],end=" " )
        print("")
    print("PRESIONE CUALQUIER TECLA PARA SEGUIR!")
    msvcrt.getch()

def validar_piso():
    os.system('cls')
    while True:
        try:
            piso = int(input("Ingrese piso(1-2): "))
            if piso in lista_pisos:
                return piso
            else:
                print("ERROR! PISO INCORRECTO!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
        print("")
        print("PRESIONE CUALQUIER TECLA PARA SEGUIR!")
        msvcrt.getch()

def validar_sala():
    os.system('cls')
    while True:
        try:
            sala = int(input("Ingrese sala(1-5): "))
            if sala in lista_sala:
                return sala
            else:
                print("ERROR! PISO INCORRECTO!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
        print("")
        print("PRESIONE CUALQUIER TECLA PARA SEGUIR!")
        msvcrt.getch()

def validar_dias():
    os.system('cls')
    while True:
        try:
            dia = int(input("Ingrese cuantos días requiere quedarse su mascota (1-60): "))
            if dia >= 1 and dia <=60:
                return dia
            else:
                print("ERROR! CANTIDAD DE DIAS INCORRECTA, DEBE ESTÁR ENTRE (1-60)!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validacion_grabar():
    if 0 not in guarderia:
        print("ERROR, GUARDERIA LLENA")
        return
    
    rut=validar_rut()
    nom=validar_nombre()
    nommasc=validar_nombre_masc
    dia=validar_dias()
    ver_guarderia()
    piso=validar_piso()
    sala=validar_sala()
    print("DATOS REGISTRADOS EXITOSAMENTE!")

    lista_ruts.append(rut)
    lista_nombres.append(nom)
    lista_nom_masc.append(nommasc)
    lista_dias.append(dia)
    lista_pisos.append(piso)
    lista_sala.append(sala)

    if guarderia[piso-1][sala-1] == 0:
        guarderia[piso-1][sala-1] = 1
    print("")
    print("PRESIONE CUALQUIER TECLA PARA SEGUIR!")
    msvcrt.getch()

def buscar():
    rut = validar_rut()
    if rut in lista_ruts:
        posicion=lista_ruts.index(rut)
        print(f"""
        SU MASCOTA SE ENCUENTRA EN: PISO {lista_pisos[posicion]} SALA {lista_sala[posicion]}""")
    else:
        print("RUT NO ENCONTRADO, FAVOR DE REGISTRARSE!")
    print("")
    print("PRESIONE CUALQUIER TECLA PARA SEGUIR!")
    msvcrt.getch()

def retirarse():
    rut = validar_rut()
    if rut in lista_ruts:
        posicion=lista_ruts.index(rut)
        monto_final={lista_dias[posicion]*vdia}
        print(f"""USTED DEBE PAGAR EL MONTO DE {monto_final}""")
        while True:
            try:
                dinero=int(input(f"INGRESE MONTO A PAGAR: {monto_final}"))
                if dinero==monto_final:
                    print("PAGO EXITOSO")
                    lista_ruts.pop(posicion)
                    lista_nombres.pop(posicion)
                    lista_nom_masc.pop(posicion)
                    lista_dias.pop(posicion)
                    lista_pisos.pop(posicion)
                    lista_sala.pop(posicion)

                    if guarderia[posicion-1][posicion-1] == 1:
                        guarderia[posicion-1][posicion-1] = 0
                    print("")
                    print("PRESIONE CUALQUIER TECLA PARA SEGUIR!")
                    msvcrt.getch()
                else:
                    print("ERROR, SU PAGO NO PUEDE EXCEDER NI SER MAS BAJO QUE EL MONTO FINAL! ")
            except:
                print("ERROR, SU MONTO DEBE SER ENTERO")
    else:
        print("RUT NO ENCONTRADO, FAVOR DE REGISTRARSE!")
    print("")
    print("PRESIONE CUALQUIER TECLA PARA SEGUIR!")
    msvcrt.getch()
    


