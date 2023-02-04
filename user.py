class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0

    def make_withdrawal(self, amount):
        if amount > self.balance:
            print(f"User: the requested amount is greater than {self.name}'s balance.")
            print(f"User: Balance = ${self.balance}")
            return False
        self.balance -= amount
        print(f"User: Successfully withdrew ${amount} from {self.name}'s balance.")
        return True
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
    
    def make_deposit(self, amount):
        self.balance += amount
        print(f"User: {self.name} deposited ${amount} to their balance.")
        print(f"User: Balance = ${self.balance}")

    def transfer_money(self, other_user, amount):
        if self.make_withdrawal(amount):
            other_user.make_deposit(amount)
            print(f"User: Money Transfered from {self.name} to {other_user.name}")
            return True
        print(f"User: Money Transfer failed")
        return False
    
elon_musk = User("Elon Musk", "elon@tesla.com")
jordan_peterson = User("Jordan Peterson" , "jordan@gmail.com")
alaa_taieb = User("Alaa Taieb", "alaataieb.tn@gmail.com")

elon_musk.make_deposit(15000000)
elon_musk.make_deposit(300000000)
elon_musk.make_deposit(1300000000)

elon_musk.make_withdrawal(45000)

elon_musk.display_user_balance()

jordan_peterson.make_deposit(200000)
jordan_peterson.make_deposit(150000)

jordan_peterson.make_withdrawal(25000)
jordan_peterson.make_withdrawal(82500)

jordan_peterson.display_user_balance()

alaa_taieb.make_deposit(333)

alaa_taieb.make_withdrawal(3)
alaa_taieb.make_withdrawal(5)
alaa_taieb.make_withdrawal(7)

alaa_taieb.display_user_balance()

elon_musk.transfer_money(alaa_taieb, 1000000000)




