import string

class Product:
    def __init__(self, name):
        self.name = name

        self.processName()

    def processName(self):
        self.numLetters = 0
        for i in range(0, len(self.name)):
            if self.name[i] in string.ascii_letters:
                self.numLetters += 1
                
        self.isEven = True if 0 == self.numLetters % 2 else False
