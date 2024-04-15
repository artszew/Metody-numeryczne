import numpy as np
import matplotlib.pyplot as plt
def wykres_funkcji (rodzaj_funkcji, f): 
    if rodzaj_funkcji == 1:
        a, b, c = -3.5, 3.5, 900
    else:
        a, b, c = -6, 6, 1200
    x = np.linspace(a, b, c)
    y = f(x)
    plt.grid(True)
    plt.xlabel('x', fontsize = 22)
    plt.xticks(fontsize = 26)
    plt.ylabel('y', fontsize = 22)
    plt.yticks(fontsize=26)
    plt.plot(x, y, label="Wykres wybranej funkcji")
    plt.title('Podgladowy wykres wybranej funkcji', fontsize=18)
    plt.show()

def wykres_z_rozwiazaniem(f, a, b, rozwiazanie):
    x = np.linspace(a, b, 1000)
    y = f(x)
    plt.grid(True)
    plt.plot(x, y, label="Wykres funkcji")
    plt.scatter(rozwiazanie, f(rozwiazanie), color='red', label="Rozwiązanie")
    plt.xlabel('x', fontsize = 20)
    plt.xticks(fontsize = 26)
    plt.ylabel('y', fontsize = 20)
    plt.yticks(fontsize=26)
    plt.title('Wykres badanej funkcji na okreslonym przedziale', fontsize = 18)
    plt.legend()
    plt.show()

def wykres_pochodnej(f , a, b):
    x = np.linspace(a, b, 1000)
    y = f(x)
    plt.grid(True)
    plt.plot(x, y, label="Wykres pochodnej")
    plt.scatter(a, f(a), color='red', label="a")
    plt.scatter(b, f(b), color='green', label="b")
    plt.xlabel('x', fontsize = 20)
    plt.xticks(fontsize = 26)
    plt.ylabel('y', fontsize = 20)
    plt.yticks(fontsize=26)
    plt.title('Wykres pochodnej funkcji na przedziale <a,b>', fontsize = 18)
    plt.legend()
    plt.show()