from abc import ABCMeta, abstractmethod
from Pizza.BasePizza import BasePizza

class Topping(BasePizza,metaclass = ABCMeta):
    @abstractmethod
    def cost(self):
        pass