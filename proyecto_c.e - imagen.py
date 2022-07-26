# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 20:31:56 2022

@author: Patricio Haro
"""
#Importacion de librerias
import matplotlib.pyplot as plt #Librerias para grficar
import matplotlib.cbook as cbook #Librerias para grficar
#carga de imagenes
with cbook.get_sample_data('C:/Users/Patricio Haro/Downloads/ProyectoCE/imagenes/serie1.jpg') as image_file:
    serieim = plt.imread(image_file)
    
with cbook.get_sample_data('C:/Users/Patricio Haro/Downloads/ProyectoCE/imagenes/paralelo.jpg') as image_file:
    paraleloim = plt.imread(image_file)

## PROGRAMA
def circuito():
    print("\n \n 'PROYECTO INTEGRADOR 'PROGRAMA DE CALCULO DE RESISTENCIAS'\n")
    print("     Seleccione el tipo de circuito que desea calcular.")
    print("        1) SERIE:                 2) PARALELO: ")
    
    opcion=int(input("Escriba la opcion: ")) 
    while opcion<1 or opcion>2:
        print("'POR FAVOR' Ingrese una opcion valida.")
        opcion=int(input("Escriba la opcion: "))
    
    if opcion==1:
       equi=serie()
       graficar(serieim)
       volta_corr(equi)
            
    else:
        equi=paralelo()
        graficar(paraleloim)
        volta_corr(equi)
    

def serie():
    print("Usted ha elegido el 'CIRCUITO SERIE'")
    resist=int(input("Ingrese el numero de 'RESISTENCIAS DEL CIRCUITO SERIE': "))
    while resist<1 or resist>10:
        print("'POR FAVOR' Ingrese una opcion valida, numero mayor a 'CERO' y menor que 'ONCE'")
        resist=int(input("Ingrese el numero de 'RESISTENCIAS DEL CIRCUITO SERIE': "))
    
    
    lista=[]
    for i in range(resist):
        print("\nIngrese el valor de la R",i+1,"(OHMS):")
        lista.append(float(input()))
        while lista[i]<1:
            print("'POR FAVOR' Ingrese una opcion valida, numero mayor a cero, no existen resistencias negativas")
            lista[i]=float(input())
            
    print("\n")
    req=0
    for j in range(resist):
        req=lista[j]+req
        print("El valor de la R",j+1,":",lista[j],"OHMS")
    print("\nLA 'RESISTENCIA EQUIVALENTE' ES: ",req,"OHMS.")
    
    return req
    
    
def paralelo():
     print("Usted ha elegido el'CIRCUITO PARALELO'")
     resist=int(input("Ingrese el numero de 'RESISTENCIAS DEL CIRCUITO PARALELO': "))
     while resist<1 or resist>10:
        print("'POR FAVOR' Ingrese una opcion valida, numero mayor a 'CERO' y menor que 'ONCE'")
        resist=int(input("Ingrese el numero de 'RESISTENCIAS DEL CIRCUITO PARALELO': "))

    
     lista=[]
     for i in range(resist):
        print("\nIngrese el valor de la R",i+1,"(OHMS):")
        lista.append(float(input()))
        while lista[i]<1:
            print("'POR FAVOR' Ingrese una opcion valida, numero mayor a cero- no existen resistencias negativas")
            lista[i]=float(input())
     
     print("\n")
     req=0
     suma=0
     for j in range(resist):
         suma=suma+(1/lista[j])
         print("El valor de la R",j+1,":",lista[j],"OHMS")
    
     req=round(1/suma,2) 
     print("\n LA RESISTENCIA EQUIVALENTE ES: ",req,"OHMS.\n")
     
     return req

def volta_corr(valor):
    
    print("\n¿Desea calcular?:\n")
    print("1) 'VOLTAJE'.        2) 'CORRIENTE'.         3) 'SALIR'.")
    opcion=int(input("Escriba la opcion: ")) 
    while opcion<1 or opcion>3:
         print("'POR FAVOR' Ingrese una opcion valida.")
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
    corr=float(input("Ingrese la corriente: "))
    vol=round(corr*res_equi,2)
    pot=round(vol*corr,2)
    
    
    print("\nLa CORRIENTE es:   ",corr,"A.")
    print("El VOLTAJE es:     ",vol,"V.")
    print("La POTENCIA es:    ",pot,"W.")
    print("La RESISTENCIA EQUIVALENTE es:",res_equi,"OHMS.")
    
    print("\nDesea continuar con otro calculo, escoja la opcion :")
    opc1=int(input(" 1) Si                        2) NO \n"))
    while opc1<1 or opc1>2:
        print("¡POR FAVOR!, Ingrese una opcion valida")
        opc1=int(input(" 1) Si                        2) NO\n"))
      
    if opc1 == 1:
        circuito()
    else :
         salida()


def calcorriente(res_equi):
    vol=float(input("Ingrese el voltaje: "))
    corr=round(vol/res_equi,2)
    pot=round(vol*corr,2)
    print("\nLa CORRIENTE es:   ",corr,"A.")
    print("El VOLTAJE es:     ",vol,"V.")
    print("La POTENCIA es:    ",pot,"W.")
    print("La RESISTENCIA EQUIVALENTE es:",res_equi,"OHMS.")
    print("\nDesea continuar con otro calculo, escoja la opcion :")
    opci2=int(input(" 1) Si                        2) NO \n"))
    while opci2<1 or opci2>2:
        print("¡POR FAVOR!, Ingrese una opcion valida")
        opc1=int(input(" 1) Si                        2) NO \n"))
      
    if opci2 == 1:
        circuito()
    else :
         salida()
    
def salida():
    print("¡GRACIAS, EXCELENTE DIA!")
   
def graficar(aux):
    fig, ax = plt.subplots()#Desinir espacio de grafico

    ax.imshow(aux) #cargar datos del grafico
    ax.axis('off')  # borar ejes x & y

    plt.show() #imprimir imagen

circuito()

    
    
    



    


