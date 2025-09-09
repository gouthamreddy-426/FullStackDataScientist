class Menu:
    def __init__(self):
        self.items = {}
    def add_item(self,name, price):
        self.items[name] = price
        print(name,"added")
    def remove_item(self,name):
        del self.items[name]
        print(name,"Removed")
    def update_price(self,name, new_price):
        self.items[name] = new_price
        print(name,"price updated to",new_price)
    def show_menu(self):
        return self.items 
    
menu = Menu()
menu.add_item("Burger", 100)
menu.add_item("Pizza", 200)
menu.update_price("Pizza", 250)
menu.remove_item("Burger")
print(menu.show_menu())