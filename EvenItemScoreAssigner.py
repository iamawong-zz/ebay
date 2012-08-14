import Customer
from ItemScoreAssigner import ItemScoreAssigner

class EvenItemScoreAssigner(ItemScoreAssigner):
    # If the product has an even number of letters, the score is given by the
    # number of vowels in the customer's name multiplied by 1.5
    def getItemScore(self, customer):
        return customer.numVowels*1.5
