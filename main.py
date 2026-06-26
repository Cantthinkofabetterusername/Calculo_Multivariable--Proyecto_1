from algoritmos import *
import cProfile
import random
import pstats

# Sabemos que T(n) >= n log2 (n) - n + 1, entonces si queremos encontrar el número n de tal forma que el número máximo de ejecuciones sea 500, entonces:
# 500 >= n log2(n) - n + 1 ---> 0 >= n log2(n) - n - 499
# Esta ecuación no se puede de resolver de manera analítica, entonces usamos el método de bisección y el método de Newton para aproximar la solución.

n = sp.symbols("n")

T_n = n*sp.log(n, 2) - n - 499

p = sp.plot(T_n, (n, -1, 200), show=False)

p.xlabel = "n"
p.ylabel = "T(n)"

p.show()

# Podemos observar con la gráfica que el valor está aproximadamente entre 85 y 95, entonces usamos los métodos númericos previamente mencionados
# para obtener las raíces:

resultado_biseccion = MetodoBiseccion(T_n, 85, 95, 1e-4, 100, n)
resultado_newton = MetodoNewton(T_n, 90, 1e-4, 100, n)

print("El resultado con Bisección fue: ", resultado_biseccion)
print("El resultado con Newton fue: ", resultado_newton, "\n")

print("El resultado discretizado es: ", int(resultado_biseccion), "\n")

# Podemos ver que con ambos métodos llegamos aproximadamente a 90.68, pero ese número no corresponde exactamente al número máximo de elementos ya que no
# tiene sentido que un array posea 90.68 elementos. Lo que sí podemos intuir es que un array con 90 elementos no puede tardar en ordenarse más de 500 pasos,
# y eso lo podemos comprobar.

for i in range(3):
    test_array = [random.randint(0, 1000) for _ in range(90)]
    profiler = cProfile.Profile()
    profiler.enable()

    merge_sort(test_array)

    profiler.disable()

    stats = pstats.Stats(profiler)
    stats.sort_stats("name").print_stats("append")

# Para mostrar que aplica para cualquier caso, vamos a hacer que el usuario ingrese el número de pasos máximos que se debe ejecutar el algoritmo:

response = True

while response:
    pasos_maximos = int(input("\nIngrese el número máximo de pasos que debe ejecutar el algoritmo: "))
    T_n = n*sp.log(n, 2) - n + 1 - pasos_maximos
    positive_product = True
    n1 = 1
    n2 = 2
    while positive_product:
        T_n1 = n1*sp.log(n1, 2) - n1 + 1 - pasos_maximos
        T_n2 = n2*sp.log(n2, 2) - n2 + 1 - pasos_maximos
        if (T_n1 * T_n2) < 0:
            interval1 = n1
            interval2 = n2
            positive_product = False
        n1 += 1
        n2 += 1
    n1_elementos = int(MetodoBiseccion(T_n, interval1, interval2, 1e-4, 100, n))
    n2_elementos = int(MetodoNewton(T_n, n1_elementos, 1e-4, 100, n))
    if n1_elementos == n2_elementos:
        print("\nAmbos métodos coinciden. Se usará el valor: ", n1_elementos, "\n")
    else:
        print("\nLos métodos no coinciden. Se usará el valor: ", n1_elementos, "\n")
    for i in range(3):
        test_array = [random.randint(0, 1000) for _ in range(n1_elementos)]
        profiler = cProfile.Profile()
        profiler.enable()
        merge_sort(test_array)
        profiler.disable()
        stats = pstats.Stats(profiler)
        stats.sort_stats("name").print_stats("append")
    y_n = input("\n¿Desea probar con otro valor? (s/n)\n")
    if y_n == "n":
        response = False
    elif y_n == "s":
        response = True
    else:
        print("\nRespuesta inválida. Se asumirá que sí.\n")