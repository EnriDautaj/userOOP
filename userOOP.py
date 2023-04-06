class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


Enri = User("Enri")
Arber = User("Arber")
Alesio= User("Alesio")

Enri.make_deposit(100)
Enri.make_deposit(200)
Enri.make_deposit(50)
Enri.make_withdrawl(45)
Enri.display_user_balance()

Arber.make_deposit(1000)
Arber.make_deposit(1000)
Arber.make_withdrawl(500)
Arber.make_withdrawl(300)
Arber.display_user_balance()

Alesio.make_deposit(1500)
Alesio.make_withdrawl(1000)
Alesio.make_withdrawl(5000)
Alesio.make_withdrawl(3000)
Alesio.display_user_balance()


Arber.transfer_money(400, Enri)