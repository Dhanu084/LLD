from abc import ABCMeta, abstractmethod

class LogProcessor(metaclass=ABCMeta):
    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self, nextLogProcessor=None):
        self.nextLogProcessor = nextLogProcessor

    @abstractmethod
    def log(self,logLevel, message):
        if self.nextLogProcessor:
            self.nextLogProcessor.log(logLevel, message)