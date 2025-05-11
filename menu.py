class MenuItem:
    def __init__(self, name:str, price:int, quantily:int):
        self.name = name
        self.price = price
        self.quantily = quantily
    
    def price_total(self)->int:
        return self.price*self.quantily
    
    def __str__(self):
        return f"{self.name}: {self.price}$"

class Appetizer(MenuItem):
    def __init__(self, name:str, price:int, quantily:int, size:str):
        super().__init__(name, price, quantily)
        self.size = size

class Drink(MenuItem):
    def __init__(self, name:str, price:int, quantily:int, type:str):
        super().__init__(name, price, quantily)
        self.type = type

class MainCourse(MenuItem):
    def __init__(self, name:str, price:int, quantily:int, vegetarian:bool, 
                family_size:bool):
        super().__init__(name, price, quantily)
        self.vegetarian = vegetarian
        self.family_size = family_size

class Dessert(MenuItem):
    def __init__(self, name:str, price:int, quantily:int, size:str):
        super().__init__(name, price, quantily)
        self.size = size

class Order:
    def __init__(self, list_menu):
        self.list_menu = list_menu
    
    def  add_items(self, item):
        self.list_menu.append(item)
    
    def total_bill_amount(self, discount:bool)->int:
        total = sum(i.price_total() for i in self.list_menu)
        return int(total*(1-discount))
    


menu = [
    Appetizer("Bruschetta", 8, 1, "Medium"),
    Appetizer("Cheese Nachos", 10, 1, "Large"),
    Drink("Coca Cola", 3, 1, "Soda"),
    Drink("Orange Juice", 4, 1, "Natural"),
    Drink("Coffee", 5, 1, "Hot"),
    MainCourse("Alfredo Pasta", 15, 1, True, False),
    MainCourse("Burger", 12, 1, False, False),
    MainCourse("Family Grill", 35, 1, False, True),
    Dessert("Chocolate Cake", 6, 1, "Medium"),
    Dessert("Vanilla Ice Cream", 4, 1, "Small"),
    Dessert("Cheesecake", 7, 1, "Large"),
    MainCourse("Caesar Salad", 10, 1, True, False)
]

orden = Order(menu)
print(orden.total_bill_amount(0.5))