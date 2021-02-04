import os
import random
import time

POLE_X = "x"
POLE_O = "o"
POLE_PUSTE = " "


def main():
    asciart("menu")
    wybor = int(input("Podaj numer: "))

    if 3 >= wybor >= 1:
        gra(wybor)

        print("Proszę podać poprawny numer.")


def gra(wybor):
    plansza, liczba_pol_planszy = stworz_plansze()
    wypisz_plansze(plansza)

    for x in range(liczba_pol_planszy):
        os.system('cls')
        wypisz_plansze(plansza)
        time.sleep(0.01)
        if wybor == 1 or wybor == 2:
            ruch_gracz(POLE_X, plansza)
        else:
            ruch_pc(POLE_X, plansza)
        os.system('cls')
        wypisz_plansze(plansza)

        if czy_koniec(plansza) is not None:
            if czy_koniec(plansza) == "Wygrał " + POLE_O:
                asciart("O")
            else:
                asciart("X")
            break

        os.system('cls')
        wypisz_plansze(plansza)
        time.sleep(0.01)
        if wybor == 2:
            ruch_gracz(POLE_O, plansza)
        else:
            ruch_pc(POLE_O, plansza)
        os.system('cls')
        wypisz_plansze(plansza)

        if czy_koniec(plansza) is not None:
            if czy_koniec(plansza) == "Wygrał " + POLE_X:
                asciart("X")
            else:
                asciart("O")
            break


def ruch_gracz(sym, plansza):  # ruch gracza
    print("Twój ruch " + sym + ", wybierz kratke i podaj:")

    kol = int(input("Kolumna: ")) - 1
    wie = int(input("Rząd: ")) - 1

    if plansza[wie][kol] == POLE_PUSTE:
        plansza[wie][kol] = sym
    elif plansza[wie][kol] != POLE_PUSTE:
        while plansza[wie][kol] != sym:
            print("To nie jest puste pole...")
            kol = int(input("Kolumna: ")) - 1
            wie = int(input("Rząd: ")) - 1
            if plansza[wie][kol] == POLE_PUSTE:
                plansza[wie][kol] = sym

    return plansza


def ruch_pc(sym, plansza): # ruch komputera
    kol = random.randint(0, len(plansza[0]) - 1)
    wie = random.randint(0, len(plansza) - 1)

    if plansza[wie][kol] == POLE_PUSTE:
        plansza[wie][kol] = sym
    elif plansza[wie][kol] != POLE_PUSTE:
        while plansza[wie][kol] != sym:
            kol = random.randint(0, len(plansza[0]) - 1)
            wie = random.randint(0, len(plansza) - 1)
            if plansza[wie][kol] == POLE_PUSTE:
                plansza[wie][kol] = sym


def stworz_plansze():  # tworzy plansze
    szer = int(input("Jakiej szerokości ma być plansza: "))
    wys = int(input("Jakiej wysokości ma być plansza: "))
    liczba_pol = wys * szer
    wiersze = []
    for x in range(0, wys):
        kolumny = []
        for y in range(0, szer):
            kolumny.append(POLE_PUSTE)
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
            if plansza[x][y] == POLE_X:
                ile_x += 1
                if ile_x == 3:
                    wynik = "Wygrał " + POLE_X
                    return wynik
                else:
                    continue
            else:
                ile_x = 0

            if plansza[x][y] == POLE_O:
                ile_o += 1
                if ile_o == 3:
                    wynik = "Wygrał " + POLE_O
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
            if plansza[y][x] == POLE_X:
                ile_x += 1
                if ile_x == 3:
                    wynik = "Wygrał " + POLE_X
                    return wynik
                else:
                    continue
            else:
                ile_x = 0
            if plansza[y][x] == POLE_O:
                ile_o += 1
                if ile_o == 3:
                    wynik = "Wygrał " + POLE_O
                    return wynik
                else:
                    continue
            else:
                ile_o = 0

    # sprawdzanie po skosie
    for x in range(len(plansza)):
        for y in range(len(plansza[0])):
            if plansza[x][y] == POLE_X:
                try:
                    if plansza[x - 1][y + 1] == POLE_X and plansza[x - 2][y + 2] == POLE_X or None:
                        wynik = "Wygrał " + POLE_X
                        return wynik
                    elif plansza[x + 1][y + 1] == POLE_X and plansza[x + 2][y + 2] == POLE_X or None:
                        wynik = "Wygrał " + POLE_X
                        return wynik
                    else:
                        continue
                except IndexError:
                    continue
            elif plansza[x][y] == POLE_O:
                try:
                    if plansza[x - 1][y + 1] == POLE_O and plansza[x - 2][y + 2] == POLE_O or None:
                        wynik = "Wygrał " + POLE_O
                        return wynik
                    elif plansza[x + 1][y + 1] == POLE_O and plansza[x + 2][y + 2] == POLE_O or None:
                        wynik = "Wygrał " + POLE_O
                        return wynik
                    else:
                        continue
                except IndexError:
                    continue


def asciart(wybor):
    if wybor == "menu":
        print("""
        +-----------------------------------------------------------------------+
        |                                                                       |
        |                                     XX     XXX                        |
        |                                       XX XX                           |
        |                                        X XX           XX              |
        |    +                                 XX   XXX       XXX               |
        |    |                                XX      XX    XXX      XX         |
        |    |  KOLKO I KRZYZYK NA STERYDZIE               XX      XX  XXX      |
        |    |  1)ROZGRYWKA Z KOMPUTEREM                  XX      XX     XX     |
        |    |  2)ROZGRYWKA Z DRUGIM GRACZEM            XX       XX       XX    |
        |    |  3)KOMPUTER VS KOMPUTER                 XX        XX       XX    |
        |    +----------------------------------->                XXX   XXX     |
        |                                                             XX        |
        |                                                                       |
        |                                                                       |
        +-----------------------------------------------------------------------+
            """)
    elif wybor == "X":
        print("""
            +-----------------------------------------------------------------------+
            |                                                                       |
            |                                                                       |
            |                                                          XXXXXXXXX    |
            |                                          XXXX         XXXXXX          |
            |    +                                         XXXXX  XXX               |
            |    |                                             XXXXX                |
            |    |                                             XXXXXXX              |
            |    |                                           XXX    XXXX            |
            |    |   WYGRAL GRACZ NR 1!!!                   XXX        XXX          |
            |    |                                          XX           XXX        |
            |    +----------------------------------->     XXX             XXX      |
            |                                              XXX              XXX     |
            |                                             XXX                 XX    |
            |                                             X                         |
            +-----------------------------------------------------------------------+
            """)
    elif wybor == "O":
        print("""
            +-----------------------------------------------------------------------+
            |                                                                       |
            |                                                  XXXXXXXXXXXX         |
            |                                                 XX          XXX       |
            |                                               XXX             XX      |
            |    +                                         XX                 X     |
            |    |                                         X                  XX    |
            |    |                                         X                   X    |
            |    |                                         X                   X    |
            |    |   WYGRAŁ GRACZ NR 2 !!!                 XX                  X    |
            |    |                                          XX                 X    |
            |    +----------------------------------->       XXX               X    |
            |                                                  XXXX          XXX    |
            |                                                     XXXXXXXXXXX       |
            |                                                                       |
            +-----------------------------------------------------------------------+
            """)


if __name__ == '__main__':
    main()
