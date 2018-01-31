from Bicycle import *

def main():
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
    TheShop.printInv()
    print('profit = {}'.format(jerry.bike.cost*TheShop.margin))
    
main()