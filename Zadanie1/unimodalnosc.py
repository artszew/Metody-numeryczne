import math
import numpy as np
from horner import horner
from wykresy import wykres_pochodnej
def unimodalnosc(rodzaj_funkcji, f, a, b):
    #funkcje podane w zadaniu sa ciagle w kazdym punkcie swojej dziedziny (widac to chocby na ich wykresach)
    #sprawdzanie ciaglosci funkcji na krancach przedzialow domknietych
    unimodalnosc = False
    if rodzaj_funkcji==1:
        granica_funkcji = lambda x: horner([1, 0, -7, 6, 0], x)
        pochodna = lambda x: horner([4, 0, -14, 6], x)
    elif rodzaj_funkcji ==2:
        granica_funkcji = lambda x: 2 * np.cos(x) - 6 * np.sin(x)
        pochodna = lambda x: -2*np.sin(x)-6*np.cos(x)
    elif rodzaj_funkcji ==3:
        granica_funkcji = lambda x: 2**x - 10
        pochodna = lambda x: math.log(2) * 2**x - 10
    else:
        granica_funkcji = lambda x: 2**x - 10*np.cos(x-20)
        pochodna = lambda x: math.log(2) * 2**x + 10*np.sin(x-20)
    if granica_funkcji(a) == f(a) and granica_funkcji(b) == f(b): #funkcja jest ciagla w przedziale domknietym<a,b>
        # sprawdzanie czy istnieje ekstremum
        wykres_pochodnej(pochodna, a, b) #warunek konieczny istnienia ekstremum
        print(f"Pochodna(a) =", pochodna(a), "Pochodna(b) =", pochodna(b))
        if (pochodna(a) * pochodna(b)) < 0: #warunek konieczny istnienia ekstremum
                unimodalnosc = True
    return unimodalnosc