import os
import random


def checkInput(type, message):
    while (True):
        try:
            data = input(f"{message} :> ")
            if(type == "int"):
                data = int(data)
            elif(type == "float"):
                data = float(data)
            elif(type == "str"):
                data = data.lower()
        except ValueError:
            showError("Error al Ingresa el Dato Intentalo de Nuevo")
        else:
            if(type == "str")and(len(data) < 1):
                showError("Error al Ingresa el Dato Intenta Ingresar Datos Reales")
            else:
                return data
        

def showSuccess(message):
    os.system("cls")
    print("\033[92m{}\033[00m" .format(message))
    os.system("pause")


def showError(message):
    os.system("cls")
    print("\033[91m{}\033[00m" .format(message))
    os.system("pause")


def showInfo(message):
    os.system("cls")
    print("\033[93m{}\033[00m" .format(message))
    os.system("pause")


def uuid():
    return random.randint(0000, 9999)

def yesORnot(message):
    os.system("cls")
    while(True):
        continuar = checkInput("str", f"{message} Si(s) o No(n)").lower()
        if continuar == "s":
            return True
        elif continuar == "n":
            return False
        else:
            showError("Error Opcion no Reconocida Ingresa s para (Si) o n Para (No)")
            


def printList(arrayText:list):
    for data in arrayText:
        print(data.upper())
    print("")
    os.system("pause")


def newDate():
    while True:
        day = checkInput("int", "Ingresa el Dia")
        if (day > 0) and (day <= 31):
            break
        else:
            showError("Ingresa un Dia Valido")
    
    while True:
        month = checkInput("int", "Ingresa el Mes")
        if (month > 0) and (month <= 12):
            break
        else:
            showError("Ingresa un Mes Valido")

    while True:
        year = checkInput("int", "Ingresa el Año")
        if (year > 2000) and (year < 3000):
            break
        else:
            showError("Ingresa un Año Ventana de Tiempo para este Campo es de (1900)-(3000)")

    return f"{day}-{month}-{year}"
