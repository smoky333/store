class Shop(object):
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Store {self.name} ,Added item: {item_name}, price: {price}")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Store {self.name} , Removed item: {name}")


    def get_price(self, item_name):

        if item_name in self.items:
            return self.items[item_name]
        else:
            print(f"Store {self.name} , Item: {item_name} not found")
            return None





    def new_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Store{self.name} , Changed price of item: {item_name} to: {new_price}")
        else:
            print(f"Store{self.name}Item: {item_name} not found")


store1 = Shop("Leclerc", "1 route de Paris")
store2 = Shop("Lidl", "42 rue de la paix")
store3 = Shop("Carrefour", "5 rue de la Croix")
store1.add_item("pomme", 2.5)
store1.add_item("poire", 1.5)
store2.add_item("sucre", 0.90)
store3.add_item("poulet", 5.0)
store1.remove_item("poire")
store1.get_price("pomme")
store1.new_price("pomme", 1.5)
print(store3.get_price("poulet"))

store1.get_price("frais")


