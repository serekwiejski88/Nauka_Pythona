import random
def main():
    wyzej_nizej()
def szukanie_losowe():
    liczba1 = random.randint(0,1000)
    liczba2 = random.randint(0,1000)
    while(not liczba2 == liczba1):

        if liczba1 > liczba2:
            message = "Nizej"
            print(message)
            liczba1 = int(input())

        elif liczba1 < liczba2:
            message = "Wyzej"
            print(message)
            liczba1 = int(input())

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