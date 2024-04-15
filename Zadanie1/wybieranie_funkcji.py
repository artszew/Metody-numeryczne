import numpy as np
from horner import horner
from wykresy import wykres_funkcji
def wybor_funkcji():
    rodzaj_funkcji = int(input(' 1 - wielomian: x^4-7*x^2+6*x \n 2 - funkcja trygonometryczna: 2cos(x)-6sin(x)\n 3 - funkcja wykladnicza: 2^x-10\n 4 - funkcja zlozona: 2^x-10cos(x-20)\n 5 - zakonczenie program\n'))
    if rodzaj_funkcji in [1, 2, 3, 4]:
        if rodzaj_funkcji == 1:  # wielomian
            wzor_funkcji = lambda x: horner([1, 0, -7, 6, 0], x)
        elif rodzaj_funkcji == 2:  # funkcja trygonometryczna
            wzor_funkcji = lambda x: 2 * np.cos(x) - 6 * np.sin(x)
        elif rodzaj_funkcji == 3:  # funkcja wykladnicza
            wzor_funkcji = lambda x: 2**x-10
        elif rodzaj_funkcji == 4:  # funkcja zlozona
            wzor_funkcji = lambda x: 2**x-10*np.cos(x-20)
        wykres_funkcji(rodzaj_funkcji, wzor_funkcji)  # podglad wykresu
    elif rodzaj_funkcji == 5:
        wzor_funkcji = None
    else:
            print(f'Musisz wybrac cyfre od 1 do 5. Sprobuj ponownie.')
            rodzaj_funkcji = int(input())
    return rodzaj_funkcji, wzor_funkcji

