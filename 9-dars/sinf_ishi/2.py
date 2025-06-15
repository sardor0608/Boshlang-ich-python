from abc import ABC, abstractmethod
class Employee(ABC):

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def calculate_bonus(self) -> float:
        pass

class Manager(Employee):

    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department=department

    def get_details(self) -> str:
        return f"Manager: {self.name}, Department: {self.department}, Salary: {self.salary}" 

    def calculate_bonus(self) -> float:
        return self.salary * 0.1


class Developer(Employee):
    def __init__(self, name, salary,programming_language ):
        super().__init__(name, salary)
        self.programming_language =programming_language 
    

    def get_details(self)->str:
        return f"Developer: {self.name}\nSalary: {self.salary}\nProgramming language: {self.programming_language}" 
    

    def calculate_bonus(self)->float:
        return self.salary*0.05


manager = Manager(name="Alice", salary=120000, department="Sales")
developer=Developer("Sardor",30_000,"Python")
print(manager.get_details())
print(manager.calculate_bonus())
print("======")
print(developer.get_details())
print(developer.calculate_bonus())

