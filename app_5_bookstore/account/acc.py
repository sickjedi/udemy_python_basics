class Account:

    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            self.commit()

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.commit()

    def commit(self):
        with open(self.file_path, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    def __init__(self, file_path, fee):
        Account.__init__(self, file_path)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
        self.commit()


checking = Checking("balance.txt", 1)
checking.transfer(100)
