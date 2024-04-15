from wybieranie_funkcji import wybor_funkcji
from kryteria import kryterium1, kryterium2
from bisekcja import bisekcja
from unimodalnosc import unimodalnosc
from zloty_podzial import zloty_podzial
from wykresy import wykres_z_rozwiazaniem

#main
if __name__ == '__main__':

    epsilon, iteracje = None, None
    print('\nWitaj w programie szukajacym miejsc zerowych rownan nieliniowych metoda bisekcji i znajdujacym minimum metoda zlotego podzialu\n')
    czesc_programu = int(input("Wybierz ktora czesc programu chcesz przetestowac: 1 - szukanie miejsc zerowych, 2 - szukanie minimum funkcji 3 - koniec programu\n"))

    glowny_program = True
    while glowny_program:

        if czesc_programu == 1:
            print("Czesc 1 programu - szukanie miejsc zerowych funkcji metoda bisekcji")
            rodzaj_funkcji, wzor_funkcji = wybor_funkcji()
            program_czesc1 = True

            while program_czesc1: #glowna petla iteracyjna
                if rodzaj_funkcji == 5: #wyjscie
                    program_czesc1 = False
                    print(f'Koniec 1. programu')
                elif rodzaj_funkcji in [1 , 2 , 3 , 4]:
                    epsilon, iteracje = kryterium1() # kryteria zatrzymania bisekcji
                    #algorytm i wykres
                    miejsce_zerowe, a, b = bisekcja(rodzaj_funkcji, wzor_funkcji, epsilon, iteracje)
                    print(f"Rozwiązanie:", miejsce_zerowe)
                    wykres_z_rozwiazaniem(wzor_funkcji, a, b, miejsce_zerowe)

                    wyjscie = int(input("Czy chcesz zakonczyc szukanie miejsc zerowych? Wpisz 1 jezeli TAK lub 2 jezeli NIE\n"))
                    if wyjscie == 1:
                        rodzaj_funkcji = 5 #koniec 1 czesci programu
                        czesc_programu = 2
                    elif wyjscie == 2: #powtorzenie programu
                        rodzaj_funkcji, wzor_funkcji=wybor_funkcji()
                    else: #bledny wybor
                        wyjscie = int(input("Zly wybor. Sprobuj jeszcze raz. Wpisz 1 jezeli chcesz opuscic program lub 2 jezeli NIE\n"))

        elif czesc_programu == 2:
            print("\nCzesc 2 programu - szukanie minimum metodą złotego podziału. Wybierz funkcje:")
            rodzaj_funkcji, wzor_funkcji = wybor_funkcji()
            program_czesc2 = True

            while program_czesc2:  # glowna petla iteracyjna
                if rodzaj_funkcji == 5:  # wyjscie
                    program_czesc2 = False
                    czesc_programu = 3
                elif rodzaj_funkcji in [1, 2, 3, 4]:
                    # przedzialy
                    a = float(input('Wprowadz lewa granice przedzialu przedzialu, od ktorego chcesz zaczac poszukiwania:\n'))
                    b = float(input('Wprowadz prawa granice przedzialu, od ktorego chcesz zaczac poszukiwania:\n'))
                    czy_unimodalna = unimodalnosc(rodzaj_funkcji, wzor_funkcji, a, b) #sprawdzenie czy funkja jest unimodalna na zadanym przedziale
                    if czy_unimodalna is True:
                        print("Twoj przedzial jest unimodalny. Przechodzimy do algorytmu zlotego podzialu.\n")
                        epsilon, iteracje = kryterium2() #kryteria zatrzymania zlotego podzialu
                        #algorytm i wykres
                        minimum=zloty_podzial(wzor_funkcji, a, b, epsilon, iteracje)
                        if minimum is not None:
                            wykres_z_rozwiazaniem(wzor_funkcji, a, b, minimum)
                        else:
                            print("Brak wykresu z powodu braku minimum")
                    else:
                        print("Funkcja nie jest unimodalna na wybranym przedziale.")
                    wyjscie = int(input("Czy chcesz zakonczyc szukanie minimum funkcji? Wpisz 1 jezeli TAK lub 2 jezeli NIE\n"))
                    if wyjscie == 1:
                        rodzaj_funkcji = 5  # koniec 2 czesci programu
                        program_czesc2 = False
                        czesc_programu = 3
                    elif wyjscie == 2:  # powtorzenie programu
                        rodzaj_funkcji, wzor_funkcji = wybor_funkcji()
                    else:  # bledny wybor
                        wyjscie = int(input("Zly wybor. Sprobuj jeszcze raz. Wpisz 1 jezeli chcesz opuscic program lub 2 jezeli NIE\n"))

        elif czesc_programu == 3:
            glowny_program = False
            print(f'Koniec programu')

        else:
            print('Zly wybor. Sprobuj ponownie\n')
            czesc_programu = int(input())
