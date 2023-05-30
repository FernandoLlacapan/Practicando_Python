import random

MIN = 0
MAX = 99

def pedir_numero(invitacion):
    while True:
        entrada = input(invitacion)
        try:
            entrada = int(entrada)
        except:
            print("Solo están autorizados los caracteres [0-9]",file=sys.stderr)
        else:
            return entrada

def pedir_numero_incognita(minimo,maximo):
    return pedir_numero_limite("Introduzca el numero a adivinar",minimo,maximo)

def pedir_numero_limite(invitacion,minimo=MIN,maximo=MAX):
    while True:
        invitacion = "{} entre {} y {} includos: ".format(invitacion,minimo,maximo)
        entrada = pedir_numero(invitacion)
        if minimo <= entrada <= maximo:
            return entrada

def jugar_una_vez(numero,minimo,maximo):
    cont = 0
    intento = pedir_numero_limite("Adivine el Numero",minimo,maximo)
    if intento < numero:
        print("Demasiado Pequeño")
        minimo = intento + 1
        victoria = False
    elif intento > numero:
        print("Demasiado Grande")
        maximo = intento - 1
        victoria = False
    else:
        print("Ha Ganado!")
        victoria = True
    return victoria,minimo,maximo

def jugar_una_partida(numero,minimo,maximo):
    while True:
        victoria,minimo,maximo = jugar_una_vez(numero,minimo,maximo)
        if victoria:
            return

def decidir_limites():
    while True:
        minimo = pedir_numero("¿Cual es el limite interior?: ")
        maximo = pedir_numero("¿Cual es el limite superior?: ")
        if maximo > minimo:
            return minimo,maximo

SI = ("s","si","y","yes","1")
def pedir_entrada_si_o_no(invitacion):
    """Por Defecto, cualque respuesta no contemplada será NO"""
    try:
        return input(invitacion).lower() in SI
    except:
        return False

def jugar():
    minimo,maximo = decidir_limites()
    while True:
        numero = pedir_numero_incognita(minimo,maximo)
        jugar_una_partida(numero,minimo,maximo)
        if not pedir_entrada_si_o_no("¿Desea Jugar una nueva Partida?: "):
            print("Hasta Pronto")
            return
def jugar_automatico(minimo,maximo):
    while True:
        numero = random.randint(minimo,maximo)
        jugar_una_partida(numero,minimo,maximo)
        if not pedir_entrada_si_o_no("¿Desea Jugar una nueva Partida?: "):
            print("Hasta Pronto")
            return        
def menu():  
    print("Adivine el numero")
    print("1- Nivel Simple (100)")
    print("2- Nivel Medio (1.000)")
    print("3- Nivel Dificil (1.000.000)")
    print("4- Nivel Experto (1.000.000.000.000)")
    opc = int(input("Opcion: "))
    if opc == 1:
        jugar_automatico(0,100)
    elif opc == 2:
        jugar_automatico(0,1000)
    elif opc == 3:
        jugar_automatico(0,1000000)
    elif opc == 4:
        jugar_automatico(0,1000000000000)
    else:
        print("Opcion equivocada\n")
        return menu()
if __name__ == '__main__':
    print("Se entró al modulo")
    menu()
else:
    print("Se importó el modulo")