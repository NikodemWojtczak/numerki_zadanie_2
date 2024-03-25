import sys
import numpy as np
import pandas as pd

df = pd.read_csv('matrix_oznaczona.csv', header=None)
A = df.iloc[:, :-1].values
b = df.iloc[:, -1].values
A = np.array(A)

print(A)
print(np.argmax(A, axis=1))

largest_indices = np.argmax(A, axis=1)
order = np.argsort(largest_indices)
A = A[order]

print(A)
print(np.argmax(A, axis=1))

expected_sequence = np.arange(0, A.shape[1])
is_sequential = np.array_equal(np.argmax(A, axis=1), expected_sequence)
if not is_sequential:
    print("Macierz nie jest zbierzna")
    sys.exit(1)

czyMniejszeOdJeden = np.all(A < 1)
if not czyMniejszeOdJeden:
    Amin = A.min()
    Amax = A.max()
    A = (A - Amin) / (Amax - Amin)
    b = (b - Amin) / (Amax - Amin)

D = np.diag(np.diag(A))
LU = np.copy(A)
np.fill_diagonal(LU, 0)
P = -np.dot(np.linalg.inv(np.copy(D)), LU)
q = np.dot(np.linalg.inv(np.copy(D)), b)
wynik = np.copy(q)
wybor = input("Podaj warunek stopu iteracje/epsilon (i/e): ")
match wybor:
    case "i":
        iterations = int(input("Podaj ilosc iteracji: "))
        for i in range(iterations):
            wynik = np.dot(P, wynik) + q
        pass
    case "e":
        wyborBledu = input("mse/mae")
        epsilon = float(input("Podaj eplison: "))
        roznica = epsilon * 2
        while roznica > epsilon:
            wynik2 = wynik
            wynik = np.dot(P, wynik) + q
            if  wyborBledu=="mae":
                roznica = np.mean(np.abs(wynik - wynik2))
            else:
                roznica = np.mean(np.square(np.abs(wynik - wynik2)))
        pass

print(f"Wynik: {wynik}")
