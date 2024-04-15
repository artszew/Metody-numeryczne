#schemat_hornera
def horner(wspolczynniki, x):
    wzor_funkcji = 0
    for i in wspolczynniki:
        wzor_funkcji = x*wzor_funkcji + i
    return wzor_funkcji #funkcja zwraca wielomian w postaci schematu hornera