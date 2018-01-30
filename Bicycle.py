class Bicycle(object): 
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
    
    def getCost(self):
        return self.cost
        
class BikeShop(object):
    def __init__(self, name, inventory, margin):
        self.name = name
        self.inventory = inventory
        self.margin = margin
    
    def printInv(self):
        for bike in self.inventory:
            print(bike.cost * self.margin)
        
    def buy(self, customer):
        for bike in self.inventory:
            if bike.cost <= customer.funds:
                self.inventory.remove(bike)
                remaining = customer.funds - bike.cost
                print(customer.funds, bike.cost, remaining, bike.model)
                return inventory
        
class Customer(object):
    def __init__(self, name, funds, bike = None):
        self.name = name
        self.funds = funds

    def afford(self,shop):
        for bike in shop.inventory:
            if bike.cost <= self.funds:
                print(self.name, bike.model, bike.cost)
      
# creating bikes    
first = Bicycle('Kids', 100, 100)
second = Bicycle('Cruiser', 100, 200)
third = Bicycle('BMX', 100, 300)
fourth = Bicycle('Mountain', 100, 500)
fifth = Bicycle('Racer', 100, 750)
sixth = Bicycle('Multi-Purpose', 100, 1000)
inventory = [first, second, third, fourth, fifth, sixth]

# creating shop
TheShop = BikeShop("The Shop", inventory, 1.2)
john = Customer('john', 200)
jerry = Customer('john', 500)
jones = Customer('john', 1000)

# testing methods    
john.afford(TheShop)
TheShop.buy(jerry)