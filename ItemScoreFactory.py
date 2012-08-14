from EvenItemScoreAssigner import EvenItemScoreAssigner
from OddItemScoreAssigner import OddItemScoreAssigner
from Product import Product

class ItemScoreFactory:
    @staticmethod
    def getItemScoreAssigner(product):
        if product.isEven:
            return EvenItemScoreAssigner()
        else:
            return OddItemScoreAssigner()
