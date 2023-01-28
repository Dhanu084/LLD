from Pizza.FarmHouse import FarmHouse
from Pizza.Margerita import Margerita
from Pizza.VegDelight import VegDelight
from Toppings.ExtraCheese import ExtraCheese
from Toppings.Mushroom import Mushroom

if __name__ == "__main__":
    base_pizza = FarmHouse()
    topping_charge = ExtraCheese( Mushroom(base_pizza)).cost()
    print(topping_charge)

    base_pizza = Margerita()
    topping_charge = ExtraCheese(base_pizza).cost()
    print(topping_charge)

    base_pizza = VegDelight()
    topping_charge = Mushroom(base_pizza).cost()
    print(topping_charge)