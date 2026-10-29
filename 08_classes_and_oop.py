#============================================================================

class BankAccount:
    counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.counter += 1
        self.account_number = BankAccount.counter

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful:", amount)
        else:
            print("Transfer failed! Insufficient balance or invalid amount.")



account1 = BankAccount("Atharv")
account2 = BankAccount("Rahul")


account1.deposit(5000)
account2.deposit(3000)


account1.withdraw(1000)


account1.transfer(2000, account2)


print("\nAccount 1 Details:")
account1.display_balance()

print("\nAccount 2 Details:")
account2.display_balance()

#============================================================================

class BankAccount:
    counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.counter += 1
        self.account_number = BankAccount.counter

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful")
        else:
            print("Insufficient balance for transfer")


a1 = BankAccount("Rahul")
a2 = BankAccount("Priya")

a1.deposit(5000)
a1.withdraw(1000)
a1.transfer(2000, a2)

print("\nAccount 1 Details:")
a1.display_balance()

print("\nAccount 2 Details:")
a2.display_balance()

#============================================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        self.display_person_info()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)



emp = Employee("Atharv", 21, 101, 30000)

emp.display_employee_info()

#============================================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        self.display_person_info()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department, team_size):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        self.team_size = team_size

    def display_manager_info(self):
        self.display_employee_info()
        print("Department:", self.department)
        print("Team Size:", self.team_size)



m = Manager("Atharv", 21, 101, 50000, "IT", 10)


m.display_manager_info()

#============================================================================

def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)

def grade(per):
    if per >= 90:
        return "A"
    elif per >= 75:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 40:
        return "D"
    else:
        return "F"
