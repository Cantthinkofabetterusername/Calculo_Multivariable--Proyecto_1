import sympy as sp
import numpy as np
from tabulate import tabulate

x = sp.symbols('x')

def MetodoBiseccion(Funcion,xizq,xder,tolerancia=1e-6,MaxPasos=100):

    Funcion = sp.lambdify(x,Funcion) #Facilite la evaluación numérica de la función
    fa =Funcion(xizq)
    fb =Funcion(xder)

    #Valores inicializados para error y pasos
    Pasos = 0
    ErrorAprox = 2
    Tabla = []  #La Tabla inicialmente está en blanco

    print('\nTabla de Resultados del Método de Bisección')
    #print('paso        a           c            b            f(a)         f(c)       f(b)   Error Aprox')  #Encabezado de la Tabla fuera del ciclo for
        
    while ErrorAprox > tolerancia and Pasos<MaxPasos:

        xc = 0.5*(xizq + xder)
        fc = Funcion(xc)
        Pasos +=1
        ErrorAprox = abs(xder-xizq)/2   #Error Estimado

        Tabla.append([Pasos,xizq,xc,xder,fa,fc,fb,ErrorAprox])  #Agregue filas a la tabla
        #print('{:3d}    {:11.8f}   {:11.8f}   {:11.8f}   {:8.2e}   {:8.2e}   {:8.2e}  {:8.2e}'. format(Pasos,xizq,xc,xder,fa,fc,fb,ErrorAprox))

        if abs(fa) <1e-16:
           xc = xizq
           print('\n La raíz se encuentra en el extremo izquierdo: ', xizq)
           break

        if abs(fb) <1e-16:
            xc= xder
            print('\n La raíz se encuentra en el extremo derecho:  ', xder)
            break

        if fa*fc<0:
            xder=xc
            fb= fc
        elif fc*fb <0:
            xizq=xc
            fa = fc
        else:
            print("El Método de Bisección falla, no hay cambio de signo en el intervalo. \n" )  
            break

    #Imprima la tabla
    print(tabulate(Tabla,headers=['Paso','a','c','b','fa','fc','fb','Error Aprox'], 
                   floatfmt=['3d','11.8f','11.8f','11.8f','8.2e','8.2e','8.2e','8.2e'],tablefmt='rounded_grid',
                   numalign='center'))

    #Resumen de resultados
    print('\n Después de {:3d} pasos, la raíz aproximada con Bisección es:  {:18.15f} \n'. format(Pasos,xc))


def MetodoNewton(Funcion,xest=0.0,TOL=1E-10,MaxPasos=100):

    Derivada = sp.diff(Funcion,x)   #Derivada con sympy
    print()
    print('La función derivada obtenida con sympy es: ')
    sp.pprint(Derivada)
    print()

    Funcion = sp.lambdify(x,Funcion) #Facilite la evaluación numérica de la función
    Derivada = sp.lambdify(x,Derivada) #Facilite la evaluación numérica de la derivada

    Pasos = 0
    Error = 2
    
    Tabla = []

    print('\nTabla de Resultados del Método de Newton')
    #print ('Paso      Estimación        Error Aproximado')
    while Error > TOL and Pasos< MaxPasos:
        Pasos += 1
        fxo =  Funcion(xest)
        dfxo = Derivada(xest)
        x1   = xest - fxo/dfxo
        Error = abs(xest-x1)
        xest   = x1  
        Tabla.append([Pasos,xest, Error])
        #print('{:2d}     {:15.12f}           {:6.2e}'. format(Pasos,xest, Error))
    

    #Imprima la tabla
    print(tabulate(Tabla,headers=['Paso','Estimación','Error Aproximado'], 
                   floatfmt=['3d','18.14f','8.2e'],tablefmt='rounded_grid',
                   numalign='center'))
    if Pasos >= 100:
        print('El Método de Newton NO pudo aproximar el valor de una raíz, intente con otra estimación.\n')
    else:
        print('Después de {:2d} pasos, la raíz aproximada con Newton es: {:14.12f} \n'. format(Pasos,xest))

    print()

    return xest

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mitad = len(arr) // 2
    izquierda = merge_sort(arr[:mitad])
    derecha = merge_sort(arr[mitad:])
    resultado = []
    i = 0
    j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado