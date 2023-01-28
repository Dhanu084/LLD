from abc import ABCMeta, abstractmethod
class IObserver(metaclass = ABCMeta):
    @abstractmethod
    def notify(self):
        pass