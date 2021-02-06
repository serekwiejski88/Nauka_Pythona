import random
import time
def main():

    current_level = 1
    number_of_tries = 7
    word = word_choice(False)
    blank_word = list("_ "*len(word))

    print(word)

    while number_of_tries>=0:
        print(levels(current_level))
        print("".join(blank_word), end='')
        print("Tries left: " + str(number_of_tries))
        pick = input("Pick a letter or write a word: ")
        if pick in word:
            index = word.index(pick)
            blank_word[index*2] = pick
            print("".join(blank_word), end='')
        else:
            number_of_tries -= 1
            current_level += 1
            print("Input does not exists in hidden word.")

            time.sleep(1)



def word_choice(bool):
    word = []
    if bool is False:
        with open('hangman.txt') as dictionary:
            list = dictionary.readlines()
            pick = list[random.randint(0, len(list)-1)].strip()
            for i in range(0,len(pick)):
                word.append(pick[i])
            return word
    else:
        pick = (input("Write a word: ")).upper()
        for i in range(0, len(pick)):
            word.append(pick[i])
        return word


def levels(num):
    level = [
    """
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    +----------------+
    """,
    """
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |  ___________   |
    |                |
    +----------------+
    """,
    """
    +----------------+
    |                |
    |    |           |
    |    |           |
    |    |           |
    |    |           |
    |  __|________   |
    |                |
    +----------------+
    """,
    """
    +----------------+
    |   ___________  |
    |    |           |
    |    |           |
    |    |           |
    |    |           |
    |  __|________   |
    |                |
    +----------------+
    """,
    """
    +----------------+
    |   ___________  |
    |    |     |     |
    |    |           |
    |    |           |
    |    |           |
    |  __|________   |
    |                |
    +----------------+
    """,
    """
    +----------------+
    |   ___________  |
    |    |     |     |
    |    |    (_)    |
    |    |           |
    |    |           |
    |  __|________   |
    |                |
    +----------------+
    """,
    """
    +----------------+
    |   ___________  |
    |    |     |     |
    |    |    (_)    |
    |    |   /|_|\   |
    |    |           |
    |  __|________   |
    |                |
    +----------------+
    """,
    """
    +----------------+
    |   ___________  |
    |    |     |     |
    |    |    (_)    |
    |    |   /|_|\   |
    |    |    | |    |
    |  __|________   |
    |     YOU LOST   |
    +----------------+
    """,
    ]
    return level[num-1]

if __name__ == '__main__':
    main()