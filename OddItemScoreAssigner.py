import Customer
from ItemScoreAssigner import ItemScoreAssigner

class OddItemScoreAssigner(ItemScoreAssigner):
    # If the item has an odd number of letters, the score is given by the number
    # of constanants in the customer's name.
    def getItemScore(self, customer):
        return customer.numConstantants;
