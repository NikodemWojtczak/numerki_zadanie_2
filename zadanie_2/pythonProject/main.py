import sys
import numpy as np
import pandas as pd

df = pd.read_csv('matrix_nieoznaczona.csv', header=None)
A = df.iloc[:, :-1].values
b = df.iloc[:, -1].values

isOk = np.all(A < 1)
if not isOk:
    print("Macierz nie jest zbierzna")
    sys.exit(1)

D = np.diag(np.diag(A))
LU = np.copy(A)
np.fill_diagonal(LU, 0)
P = -np.dot(np.linalg.inv(D), LU)
q = np.dot(np.linalg.inv(D), b)
print(f"P: {P}")
print(f"q: {q}")


wynik = np.copy(q)
wybor = input("Podaj warunek stopu iteracje/epsilon (i/e): ")
match wybor:
    case "i":
        iterations = int(input("Podaj ilosc iteracji: "))
        for i in range(iterations):
            wynik = np.dot(P, wynik) + q
        pass
    case "e":
        epsilon = float(input("Podaj eplison: "))
        roznica = epsilon * 2
        while roznica > epsilon:
            wynik2 = wynik
            wynik = np.dot(P, wynik) + q
            roznica = np.sum(np.abs(wynik - wynik2))
        pass
print(wynik)

