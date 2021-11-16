import random
import string


class passwordGenerator:
    def __init__(self):
        self.characters = []
        self.wordsFromDictionary = open("G:\\My Drive\\Project_PassKEYper\\Main_Code\\1.0.2\\PassKEYper\\usa.txt", "r")

    def numOfLettersUpper(self, amount):
        alphabetStringUpper = string.ascii_uppercase
        allLettersUpper = list(alphabetStringUpper)
        for items in range(amount):
            item = random.choice(list(allLettersUpper))
            self.characters.append(str(item))


    def numOfLettersLower(self, amount):
        alphabetStringLower = string.ascii_lowercase
        allLettersLower = list(alphabetStringLower)
        for items in range(amount):
            item = random.choice(list(allLettersLower))
            self.characters.append(str(item))


    def numOfNumbers(self, amount):
        allNumbers = {1,2,3,4,5,6,7,8,9,0}
        for items in range(amount):
            item = random.choice(tuple(allNumbers))
            self.characters.append(str(item))


    def numOfSymbols(self, amount):
        allSymbols = {'!','@','#','$','%','^','&','*','-','_',',','<','>','/','|',';',':'}
        for items in range(amount):
            item = random.choice(tuple(allSymbols))
            self.characters.append(str(item))

    def numOfWords(self, amount, caps):
        words = []
        combinedWords = []
        makeWordsCapitalized = ""

        for i in self.wordsFromDictionary:
            words.append(i.replace("\n", ""))

        for num in range(amount):
            if caps == "yes":
                for i in words:
                    if len(i) > 1:
                        randomWords = random.choice(words)
                        makeWordsCapitalized = randomWords
                self.characters.append(makeWordsCapitalized.capitalize())
            elif caps == "no":
                for i in words:
                    if len(i) > 1:
                        randomWords = random.choice(words)
                        makeWordsCapitalized = randomWords
                self.characters.append(makeWordsCapitalized)

    def generatedPassword(self):
        random.shuffle(self.characters)
        newPassword = "".join(self.characters)

        return newPassword

    def generatedMemorablePassword(self):
        newPassword = "".join(self.characters)

        return newPassword