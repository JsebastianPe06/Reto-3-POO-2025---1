# Reto-3-POO-2025---1
Aquí se encuentra el diagrama de clases del reto 3:

```mermaid
classDiagram
    class MenuItem {
        - name: string
        - price: int
        - quantily: int
        + __init__(self, name, price, quantily)
        + price_total()
        + __str__()
    }

    class Appetizer {
        - size: string
    }

    class Drink {
        - type: string
    }

    class MainCourse {
        - vegetarian: bool
        - family_size: bool
    }

    class Dessert {
        - size: string
    }

    class Order {
        - list_menu
        + __init__(self, list_menu)
        + add_items(item)
        + total_bill_amount(discount: bool)
    }

    MenuItem <|-- Appetizer
    MenuItem <|-- Drink
    MenuItem <|-- MainCourse
    MenuItem <|-- Dessert
    Order "1" o-- "*" MenuItem
