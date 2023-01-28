from abc import ABCMeta, abstractmethod

class IDriveStrategy(metaclass = ABCMeta):

    @abstractmethod
    def drive(self):
        pass