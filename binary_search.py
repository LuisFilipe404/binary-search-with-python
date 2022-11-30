import random

class BinarySearch:
    def __init__(self):
        self.listOfNumbers = []
        self.middleNumber = 0
        self.listLength = 0
        self.startNumber = 0
        self.endNumber = 0

    def generateRandomList(self): 
        self.listLength = int(input("Enter the list lenght: "))
        self.endNumber = self.listLength - 1 # position of the end of the list

        maxValue = int(input("Enter the maximum value: "))

        # generate random numbers and set them to the append of the list
        for i in range(0, self.listLength):
            randomNumber = random.randint(1, maxValue)
            self.listOfNumbers.append(randomNumber)
        
    def sortListOfNumbers(self):
        self.listOfNumbers = sorted(self.listOfNumbers)

    def getSearchNumber(self, key):

        self.middleNumber = round((self.endNumber + self.startNumber) / 2) # get the middle number

        if self.startNumber > self.endNumber:
            # if the key not exist in the list
            print("\nThe key", key, "is not in the list")
            return -1 # end cycle
        else:
            # maybe the key exists in the list
            if self.listOfNumbers[self.middleNumber] == key:
                # the key exists in the list
                print("\nThe Key", key, "is in the", self.middleNumber, "position")
                return 1
            elif self.listOfNumbers[self.middleNumber] > key:
                # discard half of the list 
                self.endNumber = self.middleNumber - 1
                return 0
            elif self.listOfNumbers[self.middleNumber] < key:
                #discard half of the list
                self.startNumber = self.middleNumber + 1
                return 0
            
    
            