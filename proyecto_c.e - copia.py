1# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 20:31:56 2022

@author: Patricio Haro
"""

def circuito():
    print("PROYECTO INTEGRADOR 'PROGRAMA DE CALCULO DE RESISTENCIAS'\n")
    print("   Seleccione el tipo de circuito que desea calcular.")
    print("        1) SERIE:                 2) PARALELO: ")
    
    opcion=int(input("Escriba la opcion: ")) 
    while opcion<1 or opcion>2:
        print("'POR FAVOR' ingrese una opcion valida.")
        opcion=int(input("Escriba la opcion:"))
    
    if opcion==1:
       equi=serie()
       volta_corr(equi)
            
    else:
        equi=paralelo()
        volta_corr(equi)
    


def serie():
    print("Usted ha elegido el 'CIRCUITO SERIE'")
    resist=int(input("Ingrese el numero de resistencias del circuito: "))
    while resist<1:
        print("'POR FAVOR' ingrese una opcion valida, numero mayor a cero:")
        resist=int(input("Ingrese el numero de resistencias del circuito: "))
    
    
    lista=[]
    for i in range(resist):
        print("\nIngrese el valor de la R",i+1,"(OHMS):")
        lista.append(int(input()))
        while lista[i]<1:
            print("'POR FAVOR' ingrese una opcion valida, numero mayor a cero, no existen resistencias negativas")
            lista[i]=int(input())
            
    print("\n")
    req=0
    for j in range(resist):
        req=lista[j]+req
        print("El valor de la R",j+1,":",lista[j],"OHMS")
    print("\nLA RESISTENCIA EQUIVALENTE ES: ",req,"OHMS.")
    
    return req
    
    
def paralelo():
     print("Usted ha elegido el'CIRCUITO PARALELO'")
     resist=int(input("Ingrese el numero de resistencias del circuito: "))
     while resist<1:
        print("'POR FAVOR' ingrese una opcion valida, numero mayor a cero:")
        resist=int(input("Ingrese el numero de resistencias del circuito: "))
    

    
     lista=[]
     for i in range(resist):
        print("\nIngrese el valor de la R",i+1,"(OHMS):")
        lista.append(int(input()))
        while lista[i]<1:
            print("'POR FAVOR' ingrese una opcion valida, numero mayor a cero- no existen resistencias negativas")
            lista[i]=int(input())
     
     print("\n")
     req=0
     suma=0
     for j in range(resist):
         suma=suma+(1/lista[j])
         print("El valor de la R",j+1,":",lista[j],"OHMS")
    
     req=1/suma ("\n")   
     print("LA RESISTENCIA EQUIVALENTE ES: ",req,"OHMS.\n")
     
     return req

def volta_corr(valor):
    
    print("\n¿Desea calcular?:\n")
    print("1) 'VOLTAJE'.        2) 'CORRIENTE'.         3) 'SALIR'.")
    opcion=int(input("Escriba la opcion: ")) 
    while opcion<1 or opcion>3:
         print("'POR FAVOR' ingrese una opcion valida.")
         opcion=int(input("Escriba la opcion:"))
    if opcion==1:
        calvoltaje(valor)
    elif opcion==2:
        calcorriente(valor)
    elif opcion==3:
        salida()
    else:
        print("GRACIAS BUEN DIA.")     
        
def calvoltaje(res_equi):
    corr=int(input("Ingrese la corriente: "))
    vol=corr*res_equi
    pot=vol*corr
    
    print("La CORRIENTE es: ",corr,"A.")
    print("El VOLTAJE es: ",vol,"V.")
    print("La POTENCIA es: ",pot,"W.")
    print("La RESISTENCIA EQUIVALENTE es:",res_equi,"OHMS.")
    
    print("Desea continuar con otro calculo, escoja la opcion :")
    opc1=int(input(" 1) Si                        2) NO \n"))
    while opc1<1 or opc1>2:
        print("Ingrese una opcion valida")
        opc1=int(input(" 1) Si                        2) NO "))
        # opc1=int(input(" 1) Si                        2) NO "))
         
    if opc1 == 1:
        circuito()
    else :
         salida()


def calcorriente(res_equi):
    vol=int(input("Ingrese el voltaje: "))
    corr=vol/res_equi
    pot=vol*corr
    print("La CORRIENTE es: ",corr,"A.")
    print("El VOLTAJE es: ",vol,"V.")
    print("La POTENCIA es: ",pot,"W.")
    print("La RESISTENCIA EQUIVALENTE es: ",res_equi,"OHMS.")
    
    print("\nDesea continuar con otro calculo, escoja la opcion :")
    opci2=int(input(" 1) Si                        2) NO "))
    while opci2<1 or opci2>2:
        print("Ingrese una opcion valida")
        opc1=int(input(" 1) Si                        2) NO "))
      
    if opci2 == 1:
        circuito()
    else :
         salida()
    
def salida():
    print("¡GRACIAS, QUE TENGA UN BUEN DIA!")
   


circuito()

    
    
    



    


