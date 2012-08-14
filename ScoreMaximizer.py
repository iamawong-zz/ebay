from Product import Product
from Customer import Customer
from ItemScoreFactory import ItemScoreFactory
from munkres import Munkres, make_cost_matrix
import fractions, sys

# This is the main class to run. The algorithm uses the Munkres module to use the Hungarian algorithm that is the crux of this suitability score calculation. The Munkres module can be found here: http://software.clapper.org/munkres/
class ScoreMaximizer:

    if __name__=='__main__':
        fileInput = open(sys.argv[1], 'r')
        for input in fileInput:
        
            splitString = input.split(';')
            customers = splitString[0].split(',')
            products = splitString[1].split(',')

            scoreMatrix = []
            for productName in products:
                product = Product(productName)
                productRow = []
                scoreAssigner = ItemScoreFactory.getItemScoreAssigner(product)
                for customerName in customers:
                    customer = Customer(customerName)
                    # If a greatest common divisor exists for two numbers and it is greater than 1, then a common factor exists
                    itemScore = 0
                    if 1 < fractions.gcd(product.numLetters, customer.numLetters):
                        itemScore = scoreAssigner.getItemScore(customer)*1.5
                    else:
                        itemScore = scoreAssigner.getItemScore(customer)
                    productRow.append(itemScore)
                scoreMatrix += [productRow]

            # Now we implement the Munkres module to calculate the maximum suitability.
            cost_matrix = make_cost_matrix(scoreMatrix, lambda cost: 10000.00 - cost)

            munkres = Munkres()
            indexes = munkres.compute(cost_matrix)
            total = 0.0
            for row, column in indexes:
                total += scoreMatrix[row][column]

            print '%.02f' % total
