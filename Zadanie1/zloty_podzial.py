import math
def zloty_podzial(f, a, b, epsilon, iteracje):
    if iteracje is None:
        epsilon = 0.0001
    i = 1
    q = (math.sqrt(5) - 1) / 2  #Stały współczynnik
    x1 = b - q * (b - a)  #Pierwszy punkt
    x2 = a + q * (b - a)  #Drugi punkt
    f_x1, f_x2 = f(x1), f(x2)
    if iteracje is None:
        przyblizenie = int(input("Przypomnij prosze, na którym miejscu po przecinku w Twojej dokladnosci epsilon znajduje sie cyfra znaczaca?\n"))
    petla = True
    while petla:
        if epsilon is not None and abs(b - a) <= epsilon:
            print('Osiagnieto zawezenie przedzialu do zadanej wartosci.')
            minimum = round(minimum, przyblizenie)
            fm = round(f(minimum), przyblizenie)
            print('\nZnalezione do tego kroku minimum rownania: x =', minimum, "f(minimum) =", fm)
            petla = False
        elif iteracje is not None and i >= iteracje:
            print('Osiagnieto maksymalna liczbe iteracji.')
            minimum = round(minimum, 4)
            fm = round(f(minimum), 4)
            print('\nZnalezione do tego kroku minimum rownania: x =', minimum, "f(minimum) =", fm)
            petla = False
        else:
            minimum = (a + b) / 2
            print(f"\nIteracja nr", i)
            print(f"x1 =",x1,"Wartosc f(x1) =", f(x1),
                       "x2 =",x2,"Wartosc f(x2) =", f(x2),
                      "\na =",a,"Wartosc f(a) =", f(a), "b =",b,"Wartosc f(b) =", f(b),
                      "\nHipotetyczne minimum =",minimum,"Hipotetyczne f(minimum) =", f(minimum))
            if f_x1 < f_x2:
                print(f"\nf(x1)<f(x2), czyli minimum znajduje sie w lewym przedziale")
                b = x2
                x2 = x1
                f_x2 = f_x1
                x1 = b - q * (b - a)
                f_x1 = f(x1)
            else:
                print(f"\nf(x1)>f(x2), czyli minimum znajduje sie w prawym przedziale")
                a = x1
                x1 = x2
                f_x1 = f_x2
                x2 = a + q * (b - a)
                f_x2 = f(x2)
            i=i+1
    return minimum
