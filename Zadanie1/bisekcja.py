def bisekcja(rodzaj_funkcji ,f, epsilon=None, iteracje=None):
    # przedzialy
    a = float(input('Wprowadz pierwszy kraniec przedzialu, od ktorego chcesz zaczac poszukiwania:\n'))
    a_przedzial_uzytkownika = a
    b = float(input('Wprowadz drugi kraniec przedzialu, od ktorego chcesz zaczac poszukiwania:\n'))
    b_przedzial_uzytkownika = b
    i = 1
    c = ((a + b) / 2)
    if iteracje is None:
        przyblizenie = int(input("Przypomnij prosze, na którym miejscu po przecinku w Twojej dokladnosci znajduje sie cyfra znaczaca?\n"))
    petla = True
    while petla:
        if epsilon is not None and abs(b - a) < epsilon:
            print('Nieudana proba.', abs(b - a),'<',epsilon, 'Osiagnieto zadany poziom dokladnosci.Najdokladniejszy wynik jaki udalo sie uzyskac to:')
            print(f'c =',c,'f(c) =',fc)
            petla = False
        elif iteracje is not None and i >= iteracje:
            print('Nieudana proba. Osiagnieto maksymalna liczbe iteracji. Najdokladniejszy wynik jaki udalo sie uzyskac to:')
            print(f'c =',c,'f(c) =',fc)
            petla = False
        elif f(a) * f(b) > 0:
            print('Warunek przeciwnych znakow na krancach przedzialu nie jest spelniony.')
            c = None
            petla = False
        else:
            if iteracje is not None:
                fc = round(f(c), 4)
            else:
                fc = round(f(c), przyblizenie)
            print(f'\nIteracja nr',i)
            print(f'Pierwszy kraniec przedzialu: a =', a, 'i f(a)=',f(a),'\nDrugi kraniec przedzialu: b =', b,'i f(b)=',f(b))
            print(f'Srodek przedzialu: c =', c,'i f(c)=',fc)
            if fc == 0:
                if iteracje is not None:
                    c=round(c,4)
                else:
                    c=round(c,przyblizenie)
                print(f'f(c)=',fc,'czyli znaleziono pierwiastek rownania (po przyblizeniu): x =', c,)
                petla = False
            elif f(a)*fc < 0:
                print(f'f(a) i f(c) maja przeciwne znaki, czyli odrzucamy przedzial (c,b)')
                b = c
            elif fc*f(b) < 0:
                print(f'f(c) i f(b) maja przeciwne znaki, czyli odrzucamy przedzial (a,c)')
                a = c
            if petla is True:
                    c = ((a + b) / 2)
                    i += 1
    return c, a_przedzial_uzytkownika , b_przedzial_uzytkownika #funkcja zwraca wartosc miejsca zerowego

