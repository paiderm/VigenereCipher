import string

def letterToNumber(letter):
    return string.ascii_uppercase.find(letter)
def numberToLetter(number):
    return string.ascii_uppercase[number]
def encryptDecryptLetter(operation, messageLetter, keyLetter):
    return numberToLetter((letterToNumber(messageLetter) + letterToNumber(keyLetter)) % 26) if operation.upper() == 'E' else numberToLetter((letterToNumber(messageLetter) - letterToNumber(keyLetter)) % 26)
def encryptWord(message, key):
    messageLetters, keyLetters, encryptedWord = [*message], [*key], ''
    for i in range(len(message)):
        encryptedWord += encryptDecryptLetter('E', messageLetters[i], keyLetters[i % len(keyLetters)]) if messageLetters[i] in string.ascii_letters else ' '
    return encryptedWord
def decryptWord(message, key):
    messageLetters, keyLetters, decryptedWord = [*message], [*key], ''
    for i in range(len(message)):
        decryptedWord += encryptDecryptLetter('D', messageLetters[i], keyLetters[i % len(keyLetters)]) if messageLetters[i] in string.ascii_letters else ' '
    return decryptedWord

def validChoice(choice):
    return choice == 'E' or choice == 'D'
def isAlphabetic(string):
    for character in string:
        if not character.isalpha() and character != ' ':
            return False
    return True
def main():
    userChoice = input("Enter an E to encrypt a message, a D to decrypt a message, and Q to quit: ").upper()
    while userChoice != 'Q':
        if validChoice(userChoice):
            key = input("Enter the Vigenere key: ").upper().replace(" ", "")
            while (not isAlphabetic(key)):
                print("Invalid response!")
                key = input("Enter the Vigenere key: ").upper().replace(" ", "")
            if userChoice == 'E':
                message = input("Enter the message to be encrypted: ").upper()
                while (not isAlphabetic(message)):
                    print("Invalid response!")
                    message = input("Enter the message to be encrypted: ").upper()
                print(encryptWord(message, key))
            if userChoice == 'D':
                message = input("Enter the cypher text to decrypt: ").upper()
                while (not isAlphabetic(message)):
                    print("Invalid response!")
                    message = input("Enter the cypher text to decrypt: ").upper()
                print(decryptWord(message, key))
        else:
            print("Invalid response!")
        userChoice = input("Enter an E to encrypt a message, a D to decrypt a message, and Q to quit: ").upper()

if __name__ == "__main__":
    main()