class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # інкапсуляція

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.owner}: +{amount}")
        else:
            print("Неправильна сума")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"{self.owner}: Недостатньо коштів")
        elif amount <= 0:
            print("Неправильна сума")
        else:
            self.__balance -= amount
            print(f"{self.owner}: -{amount}")

    def get_balance(self):
        return self.__balance


# створення акаунтів
acc1 = BankAccount("Ivan", 1000)
acc2 = BankAccount("Oleg", 500)
acc3 = BankAccount("Anna", 2000)

# тестування
acc1.deposit(200)
acc1.withdraw(500)
print(acc1.get_balance())

acc2.withdraw(600)
acc2.deposit(300)
print(acc2.get_balance())

acc3.deposit(1000)
acc3.withdraw(2500)
print(acc3.get_balance())
