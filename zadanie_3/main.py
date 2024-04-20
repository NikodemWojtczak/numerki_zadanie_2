import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data(filename):
    return pd.read_csv(filename)


def choose_function(function_type, x):
    if function_type == 'linear':
        return x
    elif function_type == 'absolute':
        return np.abs(x)
    elif function_type == 'polynomial':
        return x**3 * 0.05 - x ** 2 - 5 * x + 6  # Przykład wielomianu
    elif function_type == 'trigonometric':
        return np.sin(x)
    elif function_type == 'composition':
        return - 5 * x + 6 + np.sin(x) * 8
    else:
        raise ValueError("Nieznany typ funkcji")


def interpolate_lagrange(x_points, y_points, x_dense):
    def lagrange(x, i):
        term = 1
        for j in range(len(x_points)):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        return term

    y_interpolated = [sum(y_points[i] * lagrange(xi, i) for i in range(len(x_points))) for xi in x_dense]
    return y_interpolated


def plot_data(x_node, y_node,y_real_function,  x_dense, y_inter):
    plt.figure(figsize=(10, 6))
    plt.plot(x_node, y_node, 'o', label='Węzły')
    plt.plot(x_dense, y_real_function, label='Prawdziwa funkcja\'a')
    plt.plot(x_distance, y_inter, label='Interpolacja Lagrange\'a')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolacja danych')
    plt.show()


decision = input("Czy chcesz odczytać dane z pliku? tak/nie: ")

if decision == "tak":
    data = load_data('data.csv')
    x_distance = data['x'].values
    y_real_function = data['y'].values
    indecies = np.arange(0, len(x_distance), 5)
    x_node = x_distance[indecies]
    y_node = y_real_function[indecies]
    y_inter = interpolate_lagrange(x_node, y_node, x_distance)

else:
    minimal = int(input("Podaj minimalna wartosc wezla: "))
    maximum = int(input("Podaj maksymalna wartosc wezla: "))
    distance = int(input("Podaj odstęp między węzłami: "))
    x_node = np.arange(minimal, maximum, distance)
    x_distance = np.linspace(min(x_node), max(x_node), 300)
    function_type = input("Wybierz funkcję (linear, absolute, polynomial, trigonometric, composition): ")
    y_node = choose_function(function_type, x_node)
    y_real_function = choose_function(function_type, x_distance)
    y_inter = interpolate_lagrange(x_node, y_node, x_distance)

plot_data(x_node, y_node, y_real_function,  x_distance, y_inter)


