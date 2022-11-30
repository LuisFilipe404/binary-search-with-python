'''
Binary Search with python object oriented
Author: Luís Filipe S. de Vasconcelos
'''
from binary_search import BinarySearch # import class BinarySearch

searchNumberObject = BinarySearch()

searchNumberObject.generateRandomList()

print("\nUnordered List:", searchNumberObject.listOfNumbers)

searchNumberObject.sortListOfNumbers()

print("\nOrdered List:", searchNumberObject.listOfNumbers)

key = int(input("Insert the key that you want to search: "))

returnOfCallback = 0 # callback result

# callback method
while returnOfCallback == 0:
    returnOfCallback = searchNumberObject.getSearchNumber(key)
 
