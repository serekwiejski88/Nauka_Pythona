def main():
    print("Podaj liczbę: ")
    liczba = int(input())
    for x in range(liczba):
        if x % 15 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

main()