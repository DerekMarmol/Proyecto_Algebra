import numpy as np
from fractions import Fraction
from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt


def print_matrix(matriz, n):
    for fila in matriz:
        row = ['{}'.format(Fraction(str(val)).limit_denominator()) for val in fila]
        print(' '.join(row[:n]), "|", ' '.join(row[n:]))

def gauss_jordan(matriz):
    n = len(matriz)
    iden = np.identity(n)
    extendida = np.concatenate((matriz, iden), axis=1)
    
    print("La matriz original con la matriz identidad:")
    print_matrix(extendida, n)
    
    for i in range(n):
        max_elemento = abs(extendida[i][i])
        max_fila = i
        for k in range(i+1, n):
            if abs(extendida[k][i]) > max_elemento:
                max_elemento = abs(extendida[k][i])
                max_fila = k
        extendida[[i, max_fila]] = extendida[[max_fila, i]]
        
        for k in range(i+1, n):
            factor = -extendida[k][i]/extendida[i][i]
            for j in range(i, n*2):
                if i == j:
                    extendida[k][j] = 0
                else:
                    extendida[k][j] += factor * extendida[i][j]
        
        print("Matriz extendida después de la operación de fila", i+1, ":")
        print_matrix(extendida, n)
    
    for i in range(n-1, -1, -1):
        extendida[i] /= extendida[i][i]
        for k in range(i-1, -1, -1):
            factor = -extendida[k][i]
            for j in range(n*2):
                extendida[k][j] += factor * extendida[i][j]
        
        print("Matriz extendida después de la operación de fila", i+1, ":")
        print_matrix(extendida, n)
    
    inversa = extendida[:,n:]
    return inversa

def multiplicacion_matrices(matriz1, matriz2):
    print("Multiplicando las matrices...")
    n1, m1 = matriz1.shape
    n2, m2 = matriz2.shape
    if m1 != n2:
        print("Las matrices no se pueden multiplicar.")
        return None
    producto = np.zeros((n1, m2))
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                producto[i][j] += matriz1[i][k] * matriz2[k][j]
                print(f"Multiplicando {matriz1[i][k]} y {matriz2[k][j]} y sumando al elemento ({i+1}, {j+1}) del producto.")
                print_matrix(producto, len(producto))
    print("El producto de las matrices es:")
    print_matrix(producto, len(producto))
    return producto

def resolver_sistema_ecuaciones():
    # Pregunta al usuario si el sistema de ecuaciones es de 2x2 o 3x3
    dimension = input("¿El sistema de ecuaciones es de 2x2 o 3x3? (2/3): ")
    
    if dimension == '2':
        # Pregunta al usuario qué método quiere usar para resolver el sistema de ecuaciones
        metodo = input("¿Quieres usar el método de Gauss-Jordan o Cramer para resolver el sistema de ecuaciones? (Gauss-Jordan/Cramer): ")
        
        if metodo == 'Gauss-Jordan' or metodo == 'Cramer':
            x, y = symbols('x y')
            ecuacion1 = input("Introduce la primera ecuación en formato 'ax + by = c': ")
            ecuacion2 = input("Introduce la segunda ecuación en formato 'dx + ey = f': ")
            
            eq1 = Eq(eval(ecuacion1.replace("x", "*x").replace("y", "*y").replace("=", "-(") + ")"), 0)
            eq2 = Eq(eval(ecuacion2.replace("x", "*x").replace("y", "*y").replace("=", "-(") + ")"), 0)
            solucion = solve((eq1,eq2), (x, y))
            print(f"La solución del sistema de ecuaciones es: x = {solucion[x]}, y = {solucion[y]}")
            
            # Pregunta al usuario si desea ver una gráfica
            grafica = input("¿Deseas ver el resultado en una gráfica? (s/n): ")
            if grafica.lower() == 's':
                # Crea la gráfica
                fig, ax = plt.subplots()
                
                # Dibuja un plano cartesiano de fondo
                ax.axhline(0, color='black',linewidth=0.5)
                ax.axvline(0, color='black',linewidth=0.5)
                plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
                
                x_vals = np.linspace(-10, 10, 400)
                y_eq1_sol = solve(eq1, y)
                y_eq2_sol = solve(eq2, y)
                if y_eq1_sol and y_eq2_sol:
                    y_vals1 = [y_eq1_sol[0].subs(x, val) for val in x_vals]
                    y_vals2 = [y_eq2_sol[0].subs(x, val) for val in x_vals]
                    ax.plot(x_vals, y_vals1, label=ecuacion1)
                    ax.plot(x_vals, y_vals2, label=ecuacion2)
                    ax.scatter([solucion[x]], [solucion[y]], color='red')  # marca la solución
                    ax.legend()
                    plt.show()
                else:
                    print("No se pudo resolver una o ambas ecuaciones para 'y'. No se puede trazar la gráfica.")
        else:
            print("Método no reconocido")
    elif dimension == '3':
     metodo = input("¿Quieres usar el método de Gauss-Jordan o Cramer para resolver el sistema de ecuaciones? (Gauss-Jordan/Cramer): ")
    
    if metodo == 'Gauss-Jordan' or metodo == 'Cramer':
        x, y, z = symbols('x y z')
        ecuacion1 = input("Introduce la primera ecuación en formato 'ax + by + cz = d': ")
        ecuacion2 = input("Introduce la segunda ecuación en formato 'ex + fy + gz = h': ")
        ecuacion3 = input("Introduce la tercera ecuación en formato 'ix + jy + kz = l': ")
        

        ecuacion1 = ecuacion1.replace("x", "1x").replace("y", "1y").replace("z", "1z").replace("11", "1")
        ecuacion2 = ecuacion2.replace("x", "1x").replace("y", "1y").replace("z", "1z").replace("11", "1")
        ecuacion3 = ecuacion3.replace("x", "1x").replace("y", "1y").replace("z", "1z").replace("11", "1")
        
        eq1 = Eq(eval(ecuacion1.replace("x", "*x").replace("y", "*y").replace("z", "*z").replace("=", "-(") + ")"), 0)
        eq2 = Eq(eval(ecuacion2.replace("x", "*x").replace("y", "*y").replace("z", "*z").replace("=", "-(") + ")"), 0)
        eq3 = Eq(eval(ecuacion3.replace("x", "*x").replace("y", "*y").replace("z", "*z").replace("=", "-(") + ")"), 0)
        solucion = solve((eq1,eq2,eq3), (x, y, z))
        print(f"La solución del sistema de ecuaciones es: x = {solucion[x]}, y = {solucion[y]}, z = {solucion[z]}")
    else:
        print("Dimensión no reconocida")

def main():
    print("1. Encontrar la inversa de una matriz")
    print("2. Multiplicación de matrices")
    print("3. Resolver sistemas de ecuaciones lineales")
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        print("Encontrar la inversa de una matriz")
        matriz = np.array(eval(input("Introduce la matriz en formato [[a, b], [c, d]]: ")))
        n = len(matriz)
        print("La matriz original es:")
        print_matrix(matriz, n)
        print("Calculando la inversa de la matriz por el método de Gauss-Jordan...")
        inversa = gauss_jordan(matriz)
        print("La matriz inversa es:")
        print_matrix(inversa, n)
        
    elif opcion == 2:
        matriz1 = np.array(eval(input("Introduce la primera matriz en formato [[a, b], [c, d]]: ")))
        matriz2 = np.array(eval(input("Introduce la segunda matriz en formato [[e, f], [g, h]]: ")))
        multiplicacion_matrices(matriz1, matriz2)
        
    elif opcion == 3:
        print("Resolver sistemas de ecuaciones lineales")
        resolver_sistema_ecuaciones()
        
    else:
        print("Opción no reconocida")

if __name__ == "__main__":
    main()