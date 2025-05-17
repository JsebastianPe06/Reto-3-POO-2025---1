from typing import List

class MenuItem:
    def __init__(self, name:str, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.specific_discount:float = 0
    
    def change_discount(self,new_discount:float):
        if(new_discount < 1 and new_discount >= 0):
            self.specific_discount = new_discount
    
    def price_total(self)->float:
        return self.price*self.quantity
    
    def __str__(self):
        return f"{self.name}: {self.price}$"

class Appetizer(MenuItem):
    def __init__(self, name:str, price:float, quantity:int, size:str):
        super().__init__(name, price, quantity)
        self.size = size

class Drink(MenuItem):
    def __init__(self, name:str, price:float, quantity:int, type:str):
        super().__init__(name, price, quantity)
        self.type = type

class MainCourse(MenuItem):
    def __init__(self, name:str, price:float, quantity:int, vegetarian:bool, 
                family_size:bool):
        super().__init__(name, price, quantity)
        self.vegetarian = vegetarian
        self.family_size = family_size

class Dessert(MenuItem):
    def __init__(self, name:str, price:float, quantity:int, size:str):
        super().__init__(name, price, quantity)
        self.size = size

class Order:
    def __init__(self, list_menu:List[MenuItem]):
        self.list_menu = list_menu
    
    def  add_items(self, item):
        self.list_menu.append(item)
    
    def total_bill_amount(self)->float:
        total = sum(i.price_total()*(1-i.specific_discount)
                    for i in self.list_menu)
        return total
    
    def __str__(self):
        print_code = "Order:\n"
        for i in range(len(self.list_menu)):
            print_code += f" ({i+1}). {self.list_menu[i]}"
            if(self.list_menu[i].specific_discount != 0):
                print_code += f" (-{self.list_menu[i].specific_discount}$)"
            print_code += "\n"
        print_code += f"\n --> Account total: {self.total_bill_amount()}$"
        return print_code

#Menu
bruschetta = Appetizer("Bruschetta", 8, 1, "Medium")
cheese_nachos = Appetizer("Cheese Nachos", 10, 1, "Large")
coca_cola = Drink("Coca Cola", 3, 1, "Soda")
orange_juice = Drink("Orange Juice", 4, 1, "Natural")
coffee = Drink("Coffee", 5, 1, "Hot")
alfredo_pasta = MainCourse("Alfredo Pasta", 15, 1, True, False)
burger = MainCourse("Burger", 12, 1, False, False)
family_grill = MainCourse("Family Grill", 35, 1, False, True)
chocolate_cake = Dessert("Chocolate Cake", 6, 1, "Medium")
vanilla_ice_cream = Dessert("Vanilla Ice Cream", 4, 1, "Small")
cheesecake = Dessert("Cheesecake", 7, 1, "Large")
caesar_salad = MainCourse("Caesar Salad", 10, 1, True, False)

menu = [
    bruschetta, cheese_nachos, coca_cola, orange_juice, coffee, alfredo_pasta,
    burger, family_grill, chocolate_cake, vanilla_ice_cream, cheesecake,
    caesar_salad
]

#Discount
bruschetta.change_discount(0.15)
cheese_nachos.change_discount(0.17)
cheesecake.change_discount(0.20)


orden = Order(menu)
print(orden)
print(orden.total_bill_amount())
