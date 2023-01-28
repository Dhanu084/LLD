from Toppings.Topping import Topping

class Mushroom(Topping):
    def __init__(self, base_pizza) -> None:
        self.base_pizza = base_pizza
    def cost(self):
        return self.base_pizza.cost() + 30