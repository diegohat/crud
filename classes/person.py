from abc import ABC, abstractmethod


# abstract class
class Person(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @abstractmethod
    def __str__(self):
        return f"name:{self.__name}\tage:{self.__age}"

    @abstractmethod
    def set_name(self, name: str):
        self.__name = name

    @abstractmethod
    def get_name(self):
        return self.__name()

    @abstractmethod
    def set_age(self, age: str):
        self.__age = age

    @abstractmethod
    def get_age(self):
        return self.__age()
