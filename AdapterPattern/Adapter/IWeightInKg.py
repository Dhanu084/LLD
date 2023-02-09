from abc import ABCMeta, abstractmethod


class IWeightInKg(metaclass=ABCMeta):

    @abstractmethod
    def weight(self,weightInPounds):
        pass