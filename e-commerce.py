class Customer:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
        self.purchases = []

    def __repr__(self):
        string = "customer: "+str(self.name)+"  email: "+self.mail+"\nPurchased products:\n"
        for product in self.purchases:
            string += product.name + " "
        return string

    def purchase(self, product, inventory):
        if product in inventory.inventory:
            if inventory.inventory[product] != 0:
                inventory.inventory[product] -= 1
                self.purchases.append(product)
            else:
                print("We're run out of "+ product.name)
        else:
            print("We don't sell " + product.name)




class Product:
    def __init__(self, pname, price):
        self.name = pname
        self.price = price

    def __repr__(self):
        return "product name: "+str(self.name)+"  price: eur "+str(self.price)

class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, amount):
        if product in self.inventory:
            self.inventory[product] += amount
        else:
            self.inventory[product] = amount

    def __repr__(self):
        string = "Inventory:\n"
        for product in self.inventory: string += "product: " + product.name + "  amount: " + str(self.inventory[product])+"\n"
        return string




customer1 = Customer("joe", "joe@etc.com")
sugar1 = Product("sugar", 1)
milk1 = Product("milk", 0.9)
cream1 = Product("cream", 1.9)
inventory1 = Inventory()
inventory1.add_product(sugar1, 100)
inventory1.add_product(milk1, 133)
inventory1.add_product(sugar1, 100)



print(customer1)
print(sugar1)
print(inventory1)
customer1.purchase(sugar1,inventory1)
print(inventory1)

print(customer1)
customer1.purchase(sugar1,inventory1)
customer1.purchase(milk1,inventory1)
print(customer1)
customer1.purchase(cream1,inventory1)
print(customer1)




#algo para el nuevo branch


test=0
new testline1
new testline2
