from abc import ABCMeta, abstractmethod

class WeightInPounds(metaclass=ABCMeta):
    @abstractmethod
    def weight(self):
        pass