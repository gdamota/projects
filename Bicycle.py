class Bicycle(object): 
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
    
    def getCost(self):
        return self.cost
        
class BikeShop(object):
    def __init__(self, name, inventory = [], margin):
        self.name = name
        self.inventory = inventory
        self.margin = margin
    
    def printInv(array):
        for bike in array:
            print(array[bike])
    
    def markUp(self, margin, inventory):
        prices = []
        for bike in inventory:
            price = inventory[bike].getCost()*margin
            return prices
            
        
        
        
class Customers(object):
    __init__(self, name, funds, ownBike = True):
        self.name = name
        self.funds = funds

"""better way to do this?"""        
first = bicycle(first, 100, 100)
second = bicycle(second, 100, 200)
third = bicycle(third, 100, 300)
fourth = bicycle(fourth, 100, 500)
fifth = bicycle(fifth, 100, 750)
sixth = bicycle(sixth, 100, 1000) 

BikeShop("The Shop", inventory[first, second, thirs, fourth, fifth, sixth], 1.2)

