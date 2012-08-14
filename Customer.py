import string

class Customer:
    def __init__(self, name): 
        self.name = name
        self.processName()

    def processName(self):
        self.numVowels = 0
        self.numConstantants = 0
        
        for i in range(0, len(self.name)):
            char = self.name[i]
            if char in string.ascii_letters:
                if self.isVowel(char):
                    self.numVowels += 1
                else:
                    self.numConstantants += 1

        self.numLetters = self.numVowels + self.numConstantants

    def isVowel(self, casedChar):
        char = string.lower(casedChar)
        if 'a' == char or 'e' == char or 'i' == char or 'o' == char or 'u' == char or 'y' == char:
            return True

        return False
