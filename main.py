import Funciones
import Calculos
import sys

while True:
    menu = print("""
    ------------------------------------------------------------
    Bienvenido a la calculadora antropometrica
    ------------------------------------------------------------

    1 - Hacer una antropometria
    2 - Salir
    """)

    opcion = Funciones.check_int(0,"Una opcion")

    if opcion == 1:
        confirmacion1 = input("Usted eligio la opcion hacer antroprometia es correcto? y/n: ")
        if confirmacion1 == "y":
            nombre = Funciones.check_string(None, "Nombre")                   
            altura = Funciones.check_int(0,"Altura")
            peso = Funciones.check_mediciones(0,"peso en Kg")
            sexo = Funciones.check_sexo(None)
            edad = Funciones.check_edad(0)
            print("----------------------------------------------")
            print("         Carga de Pliegues en mm")
            print("----------------------------------------------")

            bicipital = Funciones.check_mediciones(0,"pliegue Bicipital") 
            tricipital = Funciones.check_mediciones(0,"pliegue Tricipital")
            subescapular = Funciones.check_mediciones(0,"pliegue Subescaputal")
            suprailiaco = Funciones.check_mediciones(0,"pliegue Suprailiaco")
            pantorrilla_p = Funciones.check_mediciones(0,"pliegue de la Pantorrilla")
            supraespinal = Funciones.check_mediciones(0,"pliegue Supraespinal")

            print("----------------------------------------------")
            print("         Carga de Circunferencias en cm")
            print("----------------------------------------------")

            cintura = Funciones.check_mediciones(0,"circunferencia de la Cintura")
            cadera = Funciones.check_mediciones(0,"circunferencia de la Cadera")
            pantorilla = Funciones.check_mediciones(0,"circunferencia de la Pantorrilla")
            brazo_relajado = Funciones.check_mediciones(0,"circunferencia del Brazo relajado")
            brazo_contraido = Funciones.check_mediciones(0,"circunferencia de Brazo contraido")

            print("----------------------------------------------")
            print("         Carga de Diametros en cm")
            print("----------------------------------------------")

            humero = Funciones.check_mediciones(0,"diametro del Humero")
            wrist = Funciones.check_mediciones(0,"diametro de la Muñeca")
            femur = Funciones.check_mediciones(0,"diametro del Femur")


            while True:
                metdo_ecuacion = print("""
                ----------------------------------------------
                Con que metodo quiere realizar las ecuaciones

                1 - Siri
                2 - Brosek    
                ----------------------------------------------
                """)

                opcion_ecuacion = Funciones.check_int(0,"Una opcion")
                if opcion_ecuacion == 1:
                    print("Usted a elegido el metodo Siri")
                    break
                elif opcion_ecuacion == 2:
                    print("Usted a elegido el metodo Brosek")
                    break
                else:
                    print("Porfavor seleccione una opcion correcta")
                    

            carga = print("Procesando datos......")

            print("----------------------------------------------")
            print("                 Resultados  ")
            print("----------------------------------------------")

            area_muscular_brazo = Calculos.camb(brazo_relajado,tricipital,sexo)
            masa_muscular_total = Calculos.masa_muscular_total(altura,area_muscular_brazo)
            dencidad_corporal = Calculos.dencidad_corporal(sexo,edad,tricipital,subescapular,suprailiaco,bicipital)                
            masa_grasa = Calculos.masa_grasa(opcion_ecuacion,dencidad_corporal,peso)
            masa_osea = Calculos.masa_osea(altura,wrist,femur)
            masa_residual = Calculos.masa_residual(peso,masa_muscular_total,masa_grasa,masa_osea)
            masa_libre_grasa = Calculos.masa_libre_grasa(peso,masa_grasa)
            imc = Calculos.indice_masa_corporal(peso,altura)
            icc = Calculos.indice_cintura_cadera(cintura,cadera)
            peso_ideal_max = Calculos.peso_ideal_max(altura)
            peso_ideal_min = Calculos.peso_ideal_min(altura)
            endomorfia = Calculos.endomorfia(tricipital,subescapular,supraespinal,altura)
            mesomorfia = Calculos.mesomorfia(humero,femur,tricipital,brazo_contraido,pantorilla,pantorrilla_p,altura)
            ectomorfia = Calculos.ectomorfia(peso,altura)

            
            print ("Area musuclar del brazo: " + str(area_muscular_brazo) +" Cm2 \n" 
            + "Masa muscualr: " + str(masa_muscular_total) + " Kg\n"
            + "Masa grasa: " + str(masa_grasa) + " Kg\n"
            + "Masa osea: " + str(masa_osea) +" Kg\n"
            + "Masa residual: " + str(masa_residual) +" Kg\n"
            + "Masa libre de grasa: " + str(masa_libre_grasa) +" Kg\n"
            + "IMC: " + str(imc) +" Kg/m2\n"
            + "ICC: " + str(icc) +" Kg\n"
            + "Peso ideal Max: " + str(peso_ideal_max) +" Kg\n"
            + "Peso ideal Min: " + str(peso_ideal_min) +" Kg\n"
            + "Endomorfia: " + str(endomorfia) +" Kg\n"
            + "Mesomorfia: " + str(mesomorfia) +" Kg\n"
            + "Ectomorfia: " + str(ectomorfia) +" Kg\n")

        elif confirmacion1 == "n":
            continue

        confirmacion2 = input("Desea realizar otra antropometria? y/n: ")
        confirmacion2.lower()
        if confirmacion2 == "y":
            continue
        elif confirmacion2 == "n":
            print("Muchas gracias por usar nuestro programa")
            sys.exit()
            

    elif opcion == 2:
        print("Muchas gracias por usar nuestro programa")
        sys.exit()

    else:
        print("Por favor ingresar un valor correcto")
        continue
    
