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
            print(bike.model, bike.cost * self.margin)
        
    def buy(self, customer):
        for bike in self.inventory:
            if bike.cost * self.margin <= customer.funds:
                self.inventory.remove(bike)
                remaining = customer.funds - (bike.cost*self.margin)
                customer.bike = bike
                print(customer.funds, bike.cost*self.margin, remaining, bike.model)
                return self.inventory
                return customer.bike
                
        ## script returining remaining inventory and profit
                
        
class Customer(object):
    def __init__(self, name, funds, bike = None):
        self.name = name
        self.funds = funds

    def afford(self,shop):
        for bike in shop.inventory:
            if bike.cost <= self.funds:
                print(self.name, bike.model, bike.cost)
      
