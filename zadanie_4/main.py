import math
import numpy as np
from scipy.special import roots_laguerre

def gauss_laguerre_integration(f, n):
    nodes, weights = roots_laguerre(n)
    integral = np.sum(weights * f(nodes))
    return integral

def simpson(f, a , b, N):
    # Obliczenia
    s = 0
    st = 0
    dx = (b - a) / N
    for i in range(1, N + 1):
        x = a + i * dx
        st += f(x - dx / 2)
        if i < N:
            s += f(x)
    s = dx / 6 * (f(a) + f(b) + 2 * s + 4 * st)
    return s

def simpson_expo(f, a , b, N =3):
    # Obliczenia
    s = 0
    st = 0
    dx = (b - a) / N
    for i in range(1, N + 1):
        x = a + i * dx
        st += f(x - dx / 2)*math.exp(-(x - dx / 2))
        if i < N:
            s += f(x)*math.exp(-x)
    s = dx / 6 * (f(a)*math.exp(-a) + f(b)*math.exp(-b) + 2 * s + 4 * st)
    return s

def choose_function(function_type):
    if function_type == 'linear':
        return lambda x : x
    elif function_type == 'absolute':
        return lambda x : abs(x)
    elif function_type == 'polynomial':
        return lambda x : x**3 * 0.05 - x ** 2 - 5 * x + 6 # Przykład wielomianu
    elif function_type == 'trigonometric':
        return lambda x : np.sin(x)
    elif function_type == 'composition':
        return lambda x : - 5 * x + 6 + np.sin(x) * 8
    else:
        raise ValueError("Nieznany typ funkcji")

#Wybór fnkcji
function_type = input("Wybierz funkcję (linear, absolute, polynomial, trigonometric, composition): ")
f = choose_function(function_type)

dokladnosc = float(input("Wpisz dokładność: "))


#Obliczenia kwadratury Newtona-Cotesa na określonym przedziale
n = 3
a = float(input("Wpisz początek przedziału: "))
b = float(input("Wpisz koniec przedziału: "))

simpson_previous = simpson(f, a, b, n)
n = n+1
simpson_current = simpson(f, a, b, n)

while abs(simpson_previous - simpson_current) > dokladnosc:
    simpson_previous = simpson_current
    n = n+1
    simpson_current = simpson(f, a, b, n)

print(f"N = {n}")
print(f"Wartosc = {simpson_current}\n\n")


#Obliczenia kwadratury Newtona-Cotesa na nieskończonym przedziale

n = 3
a = float(input("Wpisz a: "))
d = float(input("Wpisz delta: "))
b = a
calka = simpson_expo(f, 0, b, n)
suma = calka
while abs(calka) > dokladnosc:
    a = b
    b = a + d
    calka = simpson_expo(f, a, b, n)
    suma = suma + calka

print(f"suma = {suma}")
print(f"a = {a}")
print(f"b = {b}\n\n")


#Obliczenia kwadratury Gaussa-Laguerre'a

for n in range(2, 6):
    wartosc = gauss_laguerre_integration(f, n)
    print(f"Wezly = {n}")
    print(f"Wartosc = {wartosc}")

