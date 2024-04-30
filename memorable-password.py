import random

def readWords():
    f = open("words.txt", "r")
    words = f.readlines()
    return words

words = readWords()  

def randomWord(minLength, maxLength):
    idx = random.randint(1, len(words))
    word = words[idx - 1].strip()
    if minLength <= len(word) and len(word) <= maxLength:
        return word
    else:
        result = randomWord(minLength, maxLength)
        return result


def randomSymbol():
    symbols = ["~", "!", "#", "$", "%", "^", "&", "*", "-", "+", "=", ",", ".", "?"]
    idx = random.randint(1, len(symbols))
    symbol = symbols[idx - 1]
    return symbol

def randomDigits(digitLength):
    result = ""
    for x in range(digitLength):
        digit = random.randint(1, 9)
        result += str(digit)
    return result

def randomPassword(maxLength):
    wordLength = int((maxLength - 4) / 2)
    wordOne = randomWord(wordLength - 1, wordLength + 1)
    wordTwo = randomWord(wordLength - 1, wordLength + 1)
    digitLength = maxLength - 1 - len(wordOne) - len(wordTwo)
    digits = randomDigits(digitLength)
    result = wordOne + str(digits) + randomSymbol() + wordTwo
    return result

def randomPasswords(numberOfPasswords, maxLength):
    for x in range(numberOfPasswords):
        password = randomPassword(maxLength)
        print(password)

def checkInputType(msg, input_type=int): 
    while True:
        try: 
            return input_type (msg)
        except:  
            return 0

def getMaxLength():
    tempLength = checkInputType(input("Enter password length (max 36):"))
    if tempLength >= 8 and tempLength <= 36:
        return tempLength
    else:
        print("Input must be a number from 8 to 36!")
        return getMaxLength()
    
def getNumberOfPasswords():
    tempNum = checkInputType(input("How many passwords (max 100): "))
    if tempNum >= 1 and tempNum <= 100:
        return tempNum
    else:
        print("Input must be a number from 1 to 100!")
        return getNumberOfPasswords()

maxLength = getMaxLength()
numberOfPasswords = getNumberOfPasswords()
randomPasswords(numberOfPasswords, maxLength)

