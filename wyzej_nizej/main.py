import random
import time
def main():

    while True == True:
        print(
            """
            Wyzej nizej:
                Wybór losowy = 1
                Wybór manualny = 2
                Wybór automatyczny po pol = 3
            """)

        wybor = int(input())
        if wybor == 1:
            szukanie_losowe()
        elif wybor == 2:
            wyzej_nizej()
        elif wybor == 3:
            wybór_po_pol()
        else:
            continue


def wybór_po_pol():
    print("Komputer wybiera losową liczbe...")
    liczba1 = random.randint(0,100)
    print("Komputer wybrał liczbę: " + str(liczba1))
    liczba2 = 10
    mini = 0
    maks = 100
    while(not liczba2 == liczba1):
        time.sleep(0.5)
        if liczba1 > liczba2:
            print("Nizej")
            maks = liczba1
            liczba1 = (mini+maks) // 2.0

        elif liczba1 < liczba2:
            print("Wyzej")
            mini = liczba1
            liczba1 = (mini+maks) // 2.0
        print("Komputer wybrał liczbę: " + str(liczba1))

    print("Udało się, ukryta liczba to liczba: " + str(liczba2))

def szukanie_losowe():
    print("Komputer wybiera losową liczbe...")
    liczba1 = random.randint(0,100)
    print("Komputer wybrał liczbę: " + str(liczba1))
    liczba2 = random.randint(0,101)
    mini = 0
    maks = 100
    while(not liczba2 == liczba1):
        time.sleep(0.5)
        if liczba1 > liczba2:
            print("Nizej")
            maks = liczba1
            if mini == 0:
                liczba1 = random.randint(0, maks +1)
            else:
                liczba1 = random.randint(mini, maks +1)

        elif liczba1 < liczba2:
            print("Wyzej")
            mini = liczba1
            if maks == 100:
                liczba1 = random.randint(mini, 100 +1)
            else:
                liczba1 = random.randint(mini, maks + 1)
        print("Komputer wybrał liczbę: " + str(liczba1))

    print("Udało się, ukryta liczba to liczba: " + str(liczba2))

def wyzej_nizej():
    print("Podaj liczbe od 1 do 1000: ")
    liczba1 = int(input())
    liczba2 = random.randint(0,1000)
    while(not liczba2 == liczba1):
        if liczba1 > liczba2:
            print("Nizej")
            liczba1 = int(input())
        elif liczba1 < liczba2:
            print("Wyzej")
            liczba1 = int(input())

    else: print("Zgadles, gratulacje")
main()