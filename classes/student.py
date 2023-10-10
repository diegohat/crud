from .person import Person


class Student(Person):
    def __init__(self, name: str, age: int, reg: str):
        super().__init__(name, age)
        self.__reg = reg

    def __str__(self):
        return super().__str__()

    def set_name(self, name: str):
        super().set_name(name)

    def get_name(self):
        super().get_name()

    def set_age(self, age: str):
        super().set_age(age)

    def get_age(self):
        super().get_age()

    def set_reg(self, reg: str):
        self.__reg = reg

    def get_reg(self):
        return self.__reg
