
from prometheus_client import Enum


class User:

    def __init__(self, id, name, email) -> None:
        self.__id = id
        self.__name = name
        self.__email = email

    def getName(self):
        return self.__name
    
    def getEmail(self):
        return self.__email
