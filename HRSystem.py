from datetime import datetime
import matplotlib.pyplot as plt

class Employee:
    _id_counter = 1
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.id = Employee._id_counter
        Employee._id_counter+=1
        self.promotion_history = ["Employee"]
        self.salary_history=[(salary,datetime.now())]

    def display_info(self):
        formatted_salary = f"${self.salary:,.2f}"
        print(f"ID: {self.id}, Name: {self.name}, Salary: {formatted_salary}")

    def promote(self,department):
        salary_increase=self.salary*1.15
        promoted = Manager(self.name,salary_increase,department,self.id)
        promoted.promotion_history = self.promotion_history + ["Manager"]
        promoted.salary_history=self.salary_history+[(salary_increase,datetime.now())]
        return promoted


class Manager(Employee):
    def __init__(self, name, salary, department,emp_id):
        super().__init__(name, salary)
        self.department = department
        self.id=emp_id

    def display_info(self):
        formatted_salary = f"${self.salary:,.2f}"
        print(f"ID: {self.id}, Name: {self.name}, Salary: {formatted_salary}, Department: {self.department}")


    def promote(self,region):
        salary_increase = self.salary * 1.20
        promoted = Director(self.name,salary_increase,self.department,self.id,region)
        promoted.promotion_history = self.promotion_history + ["Director"]
        promoted.salary_history = self.salary_history + [(salary_increase, datetime.now())]
        return promoted



class Director(Manager):
    def __init__(self, name, salary, department, emp_id, region):
        super().__init__(name, salary, department, emp_id)
        self.region = region


    def display_info(self):
        formatted_salary = f"${self.salary:,.2f}"
        print(f"ID: {self.id}, Name: {self.name}, Salary: {formatted_salary}, Department: {self.department}, Region: {self.region}")


class HRSystem:
    def __init__(self):
        self.employees ={}

    def add_employee(self,employee):
        self.employees[employee.id]= employee

    def promote_employee(self,emp_id,role):
        employee = self.employees.get(emp_id)
        if isinstance(employee,Employee) and not isinstance(employee,Manager):
            self.employees[emp_id] = employee.promote(role)


        elif isinstance(employee, Manager) and not isinstance(employee, Director):
            self.employees[emp_id] = employee.promote(role)

        else:
            print(f"Employee {emp_id} cannot be promoted further.")

    def print_salary_growth(self,emp_id):
        employee = self.employees.get(emp_id)
        if not employee:
            print(f"employee ID {emp_id} not found")
            return

        salaries = [entry[0] for entry in employee.salary_history]
        dates = [entry[1] for entry in employee.salary_history]
        plt.figure(figsize=(8, 4))
        plt.plot(dates, salaries, marker='o', linestyle='-', color='blue')
        plt.title(f"Salary Growth for {employee.name}")
        plt.xlabel("Date")
        plt.ylabel("Salary")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def show_all(self):
        for emp in self.employees.values():
            emp.display_info()
            print("Promotion History:", " → ".join(emp.promotion_history))
            print("-" * 40)



emp1 = Employee("Mpho",15000)
emp2 = Employee("Aaron",25000)
emp3 = Employee("Ben",20000)


HR = HRSystem()
HR.add_employee(emp1)
HR.promote_employee(emp1.id,"Sap")
HR.promote_employee(emp1.id,"Joburg")
HR.show_all()
HR.print_salary_growth(emp1.id)



