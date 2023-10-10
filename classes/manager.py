from .student import Student
from typing import List
import sys


class Manager:
    def __init__(self, students: List[Student] = []):
        self.__students = students

    def create_student(self, name: str, age: int, reg: str):
        self.__students.append(Student(name, age, reg))
        print("Student registered.")

    def print_students(self):
        for student in self.__students:
            print(student)

    def search_student(self, reg: str):
        for student in self.__students:
            if reg == student.get_reg():
                print(student)
            else:
                print("Invalid registry.")

    def delete_student(self, reg: str):
        for student in self.__students:
            if reg == student.get_reg():
                self.__students.remove(student)
                print("Student removed.")
            else:
                print("Invalid registry.")

    def update_student(self, reg: str, name: str, age: int):
        for student in self.__students:
            if reg == student.get_reg():
                student.set_name(name)
                student.set_age(age)
                print("Student name and age updated.")
            else:
                print("Invalid registry.")

    # def update_menu(self):
    #     reg = input("Insert student registry number: ")
    #     choice = input("Update Menu:\n[0]Leave.\n")
    #     match choice:
    #         case "1":
    #             print("1")

    #         case "2":
    #             print("2")

    #         case "3":
    #             print("3")

    #         case "0":
    #             return

    #         case _:
    #             print("Invalid choice.")

    def main_menu(self):
        choice = input('''
                       Update Menu:\n
                       [1]Register Student.
                       [2]Show all Students.
                       [3]Search Student.
                       [4]Delete Student.
                       [5]Update Student.
                       [0]Leave.
                       ''')
        match choice:
            case "1":
                name = input("Insert student name: ")
                age = input("Insert student age: ")
                reg = input("Insert student registry: ")
                self.create_student(name, age, reg)

            case "2":
                self.print_students()

            case "3":
                reg = input("Insert student registry: ")
                self.search_student(reg)

            case "4":
                reg = input("Insert student registry: ")
                self.delete_student(reg)
            
            case "5":
                reg = input("Insert student registry: ")
                name = input("Insert student new name: ")
                age = input("Insert student new age: ")
                self.update_student(reg, name, age)

            case "0":
                print("Leaving...")
                sys.exit()

            case _:
                print("Invalid choice.")
