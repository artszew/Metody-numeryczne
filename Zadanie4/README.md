Implementacja całkowania numerycznego metodą Newtona-Cotesa i Gaussa.

Wytyczne do funkcjonalności:
- Kwadratury złożone Newtona-Cotesa obliczane są z dokładnością podaną przez użytkownika.
- Odbywa się to w sposób iteracyjny.
- W każdej iteracji ilość podprzedziałów na które podzielony jest przedział całkowania jest zwiększana, a otrzymany wynik całkowania porównywany jest z wynikiem z poprzedniej iteracji.
- Jeśli wynik zmienił się o mniej niż dokładność podana przez użytkownika, oznacza to że dokładność całki na podanym przedziale została obliczona z zadaną dokładnością.
- Kwadratury Gaussa obliczane są dla 2, 3, 4 i 5 węzłów.
- Konieczne jest przeskalowanie funkcji i granic całkowania na przedział [−1, 1).
- W sprawozdaniu należy porównać wyniki uzyskane za pomocą obu metod całkowania.
- Należy pamiętać, że funkcje całkowane są postaci w(x) · f(x), gdzie w(x) to funkcja wagowa, przy czym w kwadraturach Gaussa funkcja wagowa jest od razu uwzględniona w metodzie.
- Przy obliczaniu kwadratur Newtona-Cotesa trzeba więc dodać funkcję wagową.
