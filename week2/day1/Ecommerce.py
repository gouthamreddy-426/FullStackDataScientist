class Order:
    def __init__(self,d = {}):
        self.d = d
    def add(self,name,price):
        self.d[name] = price
    def remove(self,name):
        del self.d[name]
    def calculate_total(self):
        return sum(self.d.values())
    def show_items(self):
        print(self.d)

cart = Order()
cart.add("shirt",500)
cart.add("Shoes",2000)
cart.show_items()
print("Total =",cart.calculate_total())

cart.remove("Shoes")
cart.show_items()
print("Total =",cart.calculate_total())