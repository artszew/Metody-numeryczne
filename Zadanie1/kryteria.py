def kryterium1(): #bisekcja
    epsilon, iteracje = None, None
    kryterium = int(input('Wybierz kryterium zatrzymania algorytmu:\n'
                              'Wpisz 1 aby algorytm konczyl sie po spelnieniu warunku nalozonego na dokladnosc\n'
                              'Wpisz 2 aby algorytm konczyl sie po osiagnieciu zadanej liczby iteracji - wynik będzie podany z dokładnoscia do 4 miejsc po przecinku\n'))
    if kryterium in[1 , 2]:
        if kryterium == 1:
            epsilon = abs(float(input('Wprowadz warunek dokladnosci obliczen w postaci ulamka dziesietnego z jedna cyfra znaczaca (epsilon):\n')))
        elif kryterium == 2:
                iteracje = int(input('Wprowadz wybrana przez Ciebie ilosc iteracji, musi to byc liczba calkowita dodatnia:\n'))
                while iteracje <= 0:
                    print('Zla liczba. Sprobuj ponownie.\n')
                    iteracje = int(input())
    else:
        print('Zle wybrane kryterium. Spróbuj ponownie. Przypominam: 1 - warunek nalozony na dokladnosc, 2 - zadana liczba iteracji')
        kryterium = int(input())
    return epsilon, iteracje

def kryterium2(): #zloty_podzial
    epsilon, iteracje = None, None
    kryterium = int(input('Wybierz kryterium zatrzymania algorytmu:\n'
                              'Wpisz 1 aby algorytm konczyl sie po osiagnieciu zadanej liczby iteracji\n'
                              'Wpisz 2 aby algorytm konczyl sie po zawezeniu przedzialu poszukiwan do wartosci podanej przez Ciebie\n'))
    if kryterium in[1 , 2]:
        if kryterium == 1:
            iteracje = int(input('Wprowadz wybrana przez Ciebie ilosc iteracji, musi to byc liczba calkowita dodatnia:\n'))
            while iteracje <= 0:
                print('Zla liczba. Sprobuj ponownie.\n')
                iteracje = int(input())
        elif kryterium == 2:
            epsilon = float(input("Wprowadz wartość epsilon ponizej ktorej program zkonczy dzialanie: epsilon="))
    else:
        print('Zle wybrane kryterium. Spróbuj ponownie. Przypominam: 1 - zadania liczba iteracji, 2 - zawezenie do zadanego przedzialu\n')
        kryterium = int(input())
    return epsilon, iteracje
