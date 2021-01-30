def main():
    print("""
    ======================================
    ---------Basic ROT Encryption---------
    ======================================
    """)
    print("By how many letters do you want to shift your text?: ")
    shift = input()
    print("Type the string you want to encrypt: ")
    text = input()
    decryption(shift, text)


def decryption(shift, text):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    fin = ""
    shift = int(shift) % 13
    for x in range(len(text)):
        if shift < 13:
            fin += alfabet[alfabet.find(text[x]) + shift]
        else:
            fin += alfabet[alfabet.find(text[x]) - shift]
    print(fin)


main()
