import string

def letterToNumber(letter):
    return string.ascii_letters.find(letter)

def encryptLetter(messageLetter, keyLetter):
    return (letterToNumber(messageLetter) + letterToNumber(keyLetter)) % 52

def encryptWord(message, key):
    messageLetters = [*message]
    keyLetters = [*key]

    for i in range(message.len):
        encryptLetter(messageLetters[i], keyLetters[i % keyLetters.len])

def main():
    userChoice, message, key = input("(E)ncrypt, (D)ecrypt, (Q)uit: "), input("Enter the message: "), input("Enter the Key: ")
    if (userChoice.upper() == 'E'):
        encryptWord(message, key)



if __name__ == "__main__":
    main()