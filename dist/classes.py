import random

class WordReader:
    def readWords(self):
        f = open("words.txt", "r")
        words = f.readlines()
        f.close()
        return words

class RandomMethods:
    def randomWord(self, minLength, maxLength):
        wr = WordReader()
        words = wr.readWords() 
        idx = random.randint(1, len(words))
        word = words[idx - 1].strip()
        if minLength <= len(word) and len(word) <= maxLength:
            return word
        else:
            result = self.randomWord(minLength, maxLength)
            return result


    def randomSymbol(self):
        symbols = ["~", "!", "#", "$", "%", "^", "&", "*", "-", "+", "=", ",", ".", "?"]
        idx = random.randint(1, len(symbols))
        symbol = symbols[idx - 1]
        return symbol

    def randomDigits(self, digitLength):
        result = ""
        for x in range(digitLength):
            digit = random.randint(1, 9)
            result += str(digit)
        return result

    def randomPassword(self, maxLength):
        wordLength = int((maxLength - 4) / 2)
        wordOne = self.randomWord(wordLength - 1, wordLength + 1)
        wordTwo = self.randomWord(wordLength - 1, wordLength + 1)
        digitLength = maxLength - 1 - len(wordOne) - len(wordTwo)
        digits = self.randomDigits(digitLength)
        result = wordOne + str(digits) + self.randomSymbol() + wordTwo
        return result

    def randomPasswords(self, numberOfPasswords, maxLength):
        for x in range(numberOfPasswords):
            password = self.randomPassword(maxLength)
            print(password)

class UserInput:
    def checkInputType(self, msg, input_type=int): 
        while True:
            try: 
                return input_type (msg)
            except:  
                return 0

    def getMaxLength(self):
        tempLength = self.checkInputType(input("Enter password length (max 36):"))
        if tempLength >= 8 and tempLength <= 36:
            return tempLength
        else:
            print("Input must be a number from 8 to 36!")
            return self.getMaxLength()
        
    def getNumberOfPasswords(self):
        tempNum = self.checkInputType(input("How many passwords (max 100): "))
        if tempNum >= 1 and tempNum <= 100:
            return tempNum
        else:
            print("Input must be a number from 1 to 100!")
            return self.getNumberOfPasswords()