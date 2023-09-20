import re


def check_string(self,entrada):
    while True:
        entrada = self.entry.get()
        if re.search(r'\d', entrada):
            print("El valor contiene numeros, por favor ingrese el valor correctamente")   
            False
        else:
            entrada.isalpha() == True
            return True
        
def check_int(self,num):
    while True:
        num = self.entry.get()
        try:
            num_entero = int (num)
            break
        except ValueError:
            print("El numero ingresado no es un entero valido")
    return num_entero

        
def check_mediciones(self,valor):
    while True:
        valor = self.entr.get()
        try:
            num_decimal = float(valor)
            break
        except ValueError:
            print("Ingrese un numero valido")
    return num_decimal

    
def check_edad(self,edad):
   
    while True:
        edad = input("Ingrese edad: ")
        try:
            edad = int(edad)
            if edad >= 17:
                return edad
            else:
                print("Debe ser mayor de 17 años, para hacer la medicion")
        except ValueError:
            print("Por favor ingrese un valor correcto")