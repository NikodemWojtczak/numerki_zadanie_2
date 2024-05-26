import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_laguerre, roots_laguerre
import math

# Funkcje do aproksymacji
def linear(x):
    return 2 * x + 1

def absolute(x):
    return np.abs(x)

def polynomial(x):
    return x ** 3 - 2 * x ** 2 + x + 5

def trigonometric(x):
    return np.sin(x)

def combined(x):
    return linear(x) + absolute(x) + polynomial(x) + trigonometric(x)

# Schemat Hornera do obliczania wartości wielomianu
def horner(coeffs, x):
    result = 0
    for coeff in coeffs:
        result = result * x + coeff
    return result

# Metoda całkowania: kwadratura Gaussa-Laguerre'a
def gauss_laguerre_integration(f, n):
    nodes, weights = roots_laguerre(n)
    integral = np.sum(weights * f(nodes))
    return integral

# Obliczanie współczynników wielomianu aproksymacyjnego
def laguerre_coefficients(f, m, n):
    coeffs = []
    for k in range(m + 1):
        integrand = lambda x: f(x) * eval_laguerre(k, x) * np.exp(-x)
        integral = gauss_laguerre_integration(integrand, n)
        coeff = integral / np.math.factorial(k)
        coeffs.append(coeff)
    return coeffs

# Główna funkcja aproksymacji
def approximate_function(f, a, b, m, n):
    coeffs = laguerre_coefficients(f, m, n)
    approx_f = lambda x: horner(coeffs[::-1], x)

    x_vals = np.linspace(a, b, 400)
    y_true = f(x_vals)
    y_approx = [approx_f(x) for x in x_vals]

    plt.plot(x_vals, y_true, label='Original Function')
    plt.plot(x_vals, y_approx, label='Laguerre Approximation')
    plt.legend()
    plt.show()

    error = np.sqrt(np.mean((y_true - y_approx) ** 2))
    print(f'Approximation Error: {error}')
    return coeffs

# Menu wyboru dla użytkownika
def user_menu():
    functions = {
        '1': linear,
        '2': absolute,
        '3': polynomial,
        '4': trigonometric,
        '5': combined
    }

    print("Choose a function to approximate:")
    print("1: Linear 2 * x + 1")
    print("2: Absolute np.abs(x)")
    print("3: Polynomial x ** 3 - 2 * x ** 2 + x + 5")
    print("4: Trigonometric np.sin(x)")
    print("5: Combined linear(x) + absolute(x) + polynomial(x) + trigonometric(x)")

    choice = input("Enter your choice (1-5): ")
    if choice not in functions:
        print("Invalid choice.")
        return

    f = functions[choice]

    a = float(input("Enter the start of the interval: "))
    b = float(input("Enter the end of the interval: "))
    m = int(input("Enter the degree of the approximating polynomial: "))
    n = int(input("Enter the number of nodes for integration: "))

    coeffs = approximate_function(f, a, b, m, n)
    print("Coefficients of the approximating polynomial:")
    print(coeffs)

# Uruchomienie programu
if __name__ == "__main__":
    user_menu()
