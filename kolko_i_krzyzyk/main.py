import os
import random

def main():
    print("""
+-----------------------------------------------------------------------+
|                                                                       |
|                                     XX     XXX                        |
|                                       XX XX                           |
|                                        X XX           XX              |
|    +                                 XX   XXX       XXX               |
|    |  KOLKO I KRZYZYK NA STERYDZIE  XX      XX    XXX      XX         |
|    |                                             XX      XX  XXX      |
|    |     1)ROZGRYWKA Z KOMPUTEREM               XX      XX     XX     |
|    |     2)ROZGRYWKA Z DRUGIM GRACZEM         XX        X       XX    |
|    |                                         XX         XX      XX    |
|    +----------------------------------->                 XXX  XXX     |
|                                                             XX        |
|                                                                       |
|                                                                       |
+-----------------------------------------------------------------------+
    """)
    wybor = int(input("Podaj numer: "))
    if wybor == 2:
        gra_1v1()


def gra_1v1():
    plansza, liczba_pol_planszy = stworz_plansze()
    wypisz_plansze(plansza)

    for x in range(liczba_pol_planszy // 2):
        os.system('cls')
        wypisz_plansze(plansza)
        ruch_x(plansza)

        if czy_koniec(plansza) is not None:
            print(czy_koniec(plansza))
            break

        os.system('cls')
        wypisz_plansze(plansza)
        ruch_o(plansza)

        if czy_koniec(plansza) is not None:
            print(czy_koniec(plansza))
            break


def ruch_x(plansza):  # ruch krzyżyka
    print("Twój ruch (x), wybierz kratke i podaj:")

    kol = int(input("Kolumna: ")) - 1
    wie = int(input("Rząd: ")) - 1

    if plansza[wie][kol] == " ":
        plansza[wie][kol] = "x"
    elif plansza[wie][kol] != " ":
        while plansza[wie][kol] != "x":
            print("To nie jest puste pole...")
            kol = int(input("Kolumna: ")) - 1
            wie = int(input("Rząd: ")) - 1
            if plansza[wie][kol] == " ":
                plansza[wie][kol] = "x"

    return plansza


def ruch_o(plansza):   # ruch kółka

    print("Twój ruch (o), wybierz kratke i podaj:")

    kol = int(input("Kolumna: ")) - 1
    wie = int(input("Rząd: ")) - 1

    if plansza[wie][kol] == " ":
        plansza[wie][kol] = "o"
    elif plansza[wie][kol] != " ":
        while plansza[wie][kol] != "o":
            print("To nie jest puste pole...")
            kol = int(input("Kolumna: ")) - 1
            wie = int(input("Rząd: ")) - 1
            if plansza[wie][kol] == " ":
                plansza[wie][kol] = "o"

    return plansza


def stworz_plansze():  # tworzy plansze
    szer = int(input("Jakiej szerokości ma być plansza: "))
    wys = int(input("Jakiej wysokości ma być plansza: "))
    liczba_pol = wys * szer
    wiersze = []
    for x in range(0, wys):
        kolumny = []
        for y in range(0, szer):
            kolumny.append(" ")
        wiersze.append(kolumny)

    return wiersze, liczba_pol


def wypisz_plansze(plansza):  # wypisuje plansze

    for x in range(len(plansza)):
        for y in range(len(plansza[0])):
            print("| " + plansza[x][y] + " |", end='')
        print("")


def czy_koniec(plansza):  # sprawdza czy trzy znaki następują po sobie pionowo poziomo i po skosie
    ile_x = 0
    ile_o = 0

    # sprawdzanie poziome
    for x in range(len(plansza)):
        for y in range(len(plansza[0])):
            if plansza[x][y] == "x":
                ile_x += 1
                if ile_x == 3:
                    wynik = "Wygrał x"
                    return wynik
                else:
                    continue
            else:
                ile_x = 0

            if plansza[x][y] == "o":
                ile_o += 1
                if ile_o == 3:
                    wynik = "Wygrał o"
                    return wynik
                else:
                    continue
            else:
                ile_o = 0
    ile_x = 0
    ile_o = 0

    # sprawdzanie pionowe
    for x in range(len(plansza[0])):
        for y in range(len(plansza)):
            if plansza[y][x] == "x":
                ile_x += 1
                if ile_x == 3:
                    wynik = "Wygrał x"
                    return wynik
                else:
                    continue
            else:
                ile_x = 0
            if plansza[y][x] == "o":
                ile_o += 1
                if ile_o == 3:
                    wynik = "Wygrał o"
                    return wynik
                else:
                    continue
            else:
                ile_o = 0

    # sprawdzanie po skosie
    for x in range(len(plansza)):
        for y in range(len(plansza[0])):
            if plansza[x][y] == "x":
                try:
                    if plansza[x-1][y+1] == "x" and plansza[x-2][y+2] == "x" or None:
                        wynik = "Wygrał x"
                        return wynik
                    elif plansza[x+1][y+1] == "x" and plansza[x+2][y+2] == "x" or None:
                        wynik = "Wygrał x"
                        return wynik
                    else:
                        continue
                except IndexError:
                    continue
            elif plansza[x][y] == "o":
                try:
                    if plansza[x - 1][y + 1] == "o" and plansza[x - 2][y + 2] == "o" or None:
                        wynik = "Wygrał o"
                        return wynik
                    elif plansza[x + 1][y + 1] == "o" and plansza[x + 2][y + 2] == "o" or None:
                        wynik = "Wygrał o"
                        return wynik
                    else:
                        continue
                except IndexError:
                    continue


if __name__ == '__main__':
    main()