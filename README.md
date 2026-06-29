# Calculo_Multivariable--Proyecto_1
Proyecto 1 de cálculo multivariable.

Reporte de Laboratorio — Métodos Numéricos
Cálculo del número máximo de elementos ordenables por Merge Sort
Métodos de Bisección y Newton

1. Introducción
El objetivo de este laboratorio es determinar el número máximo de elementos que un arreglo puede tener para que el algoritmo Merge Sort lo ordene sin superar una cantidad fija de operaciones. Esto se plantea como un problema de búsqueda de raíces, donde la incógnita es justamente ese número de elementos.
Merge Sort tiene una complejidad en el peor caso acotada por la expresión:
T(n) ≥ n·log₂(n) − n + 1
donde n es el número de elementos y T(n) representa el número de comparaciones (pasos) en el peor caso. Si fijamos un límite de 500 pasos, queremos encontrar el valor de n para el cual la cota se cumple con igualdad. Igualando y pasando todo a un solo lado obtenemos la ecuación cuya raíz buscamos:
f(n) = n·log₂(n) − n + 1 − 500 = 0
Esta ecuación es trascendental: mezcla un término lineal con un término logarítmico multiplicado por la variable, por lo que no se puede despejar n de forma analítica. Por eso recurrimos a métodos numéricos para aproximar su raíz.
Antes de aplicar los métodos, graficamos la función para ubicar visualmente dónde cruza el eje horizontal y así elegir un intervalo y un punto inicial razonables. La gráfica muestra que la raíz se encuentra aproximadamente entre n = 85 y n = 95, cruzando el eje cerca de n ≈ 90. Con esta información elegimos el intervalo [85, 95] para Bisección y el valor inicial n₀ = 90 para Newton.

2. Resultados
Resolví la ecuación con dos métodos numéricos. En ambos casos registré cómo disminuye el error en cada iteración, tomando como referencia la raíz de alta precisión n ≈ 90.68202029.
2.1 Método de Bisección
La Bisección parte de un intervalo [a, b] donde la función cambia de signo y lo divide a la mitad repetidamente, conservando el subintervalo donde sigue ocurriendo el cambio de signo. Es un método seguro pero lento, porque el error se reduce a la mitad en cada paso (convergencia lineal). Partiendo de [85, 95] con tolerancia 1×10⁻⁴:
Iterabc (punto medio)f(c)Error |c−raíz|185.0000095.0000090.00000−4.7332216.82e-01290.0000095.0000092.50000+12.6527851.82e+00390.0000092.5000091.25000+3.9474305.68e-01490.0000091.2500090.62500−0.3960055.70e-02590.6250091.2500090.93750+1.7749382.55e-01690.6250090.9375090.78125+0.6892729.92e-02790.6250090.7812590.70313+0.1465852.11e-02890.6250090.7031390.66406−0.1247221.80e-02990.6640690.7031390.68359+0.0109281.57e-031090.6640690.6835990.67383−0.0568988.19e-031190.6738390.6835990.67871−0.0229853.31e-031290.6787190.6835990.68115−0.0060288.68e-041390.6811590.6835990.68237+0.0024503.53e-041490.6811590.6823790.68176−0.0017892.58e-041590.6817690.6823790.68207+0.0003304.76e-05
La Bisección necesitó 15 iteraciones para alcanzar la tolerancia. Se observa que el error no baja de forma perfectamente monótona (sube y baja según hacia qué lado quede el punto medio), pero la tendencia general es de reducción constante.
2.2 Método de Newton
El método de Newton usa la derivada de la función para trazar una recta tangente y saltar directamente hacia la raíz. La derivada de f(n) es:
f′(n) = log₂(n) + 1/ln(2) − 1
Partiendo de n₀ = 90:
Iterxₙf(xₙ)xₙ₊₁Error190.00000000−4.73322190.682556565.36e-04290.68255656+0.00372590.682020293.29e-10
Newton convergió en apenas 2 iteraciones. El error cae de forma mucho más agresiva (convergencia cuadrática): en la segunda iteración ya alcanza una precisión cercana a 10⁻¹⁰, muy por debajo de la tolerancia pedida.
2.3 Interpretación del resultado y comprobación
Ambos métodos llegan al mismo valor: n ≈ 90.68. Sin embargo, este número no tiene sentido físico directo, porque un arreglo no puede tener 90.68 elementos. Lo que sí podemos afirmar es que un arreglo de 90 elementos no debería superar los 500 pasos al ordenarse, por lo que el valor se discretiza tomando la parte entera: n = 90.
Para comprobarlo, en el código se generan arreglos aleatorios de 90 elementos y se ordenan con Merge Sort usando cProfile, contando las operaciones reales. Además, el programa permite que el usuario ingrese cualquier límite de pasos: el código busca automáticamente un intervalo con cambio de signo, aplica Bisección y Newton, verifica que ambos coincidan y vuelve a perfilar el algoritmo con el nuevo tamaño. Las líneas clave son:
resultado_biseccion = MetodoBiseccion(T_n, 85, 95, 1e-4, 100, n)
resultado_newton = MetodoNewton(T_n, 90, 1e-4, 100, n)

3. Conclusiones

Ambos métodos convergen a la misma raíz (n ≈ 90.68), lo que confirma que la solución es correcta y consistente entre métodos.
Newton fue claramente más eficiente: resolvió el problema en 2 iteraciones frente a las 15 de Bisección, gracias a su convergencia cuadrática frente a la convergencia lineal de Bisección.
La principal limitación de Newton es que requiere la derivada y un punto inicial cercano a la raíz; si se elige mal el punto de partida puede diverger o saltar a otra raíz. La Bisección, en cambio, no necesita derivada y siempre converge si el intervalo inicial tiene cambio de signo, pero es lenta.
El resultado numérico (90.68) debe discretizarse a 90 para tener sentido en el contexto del problema, ya que el número de elementos de un arreglo es un entero.
El valor teórico coincide con lo esperado: un arreglo de 90 elementos se mantiene dentro del límite de 500 pasos al ordenarse con Merge Sort, lo cual se verifica empíricamente con el perfilado por cProfile en el programa.


4. Programa
El modelo y los métodos se implementaron en Python, apoyándose en SymPy para el manejo simbólico de la función y su derivada, y en cProfile para medir el número real de operaciones del Merge Sort. Las líneas de código más relevantes son las llamadas a MetodoBiseccion y MetodoNewton mostradas arriba, junto con el bloque interactivo que permite al usuario probar distintos límites de pasos y reordenar arreglos del tamaño calculado.