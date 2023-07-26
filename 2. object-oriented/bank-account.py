class Customer:
    def __init__(self, name, iden, ac_no) -> None:
        self.name = name
        self.id = iden
        self.ac_no = ac_no
    def display(self):
        print("Customer Name: ", self.name)
        print("Customer ID: ", self.id)
        print("Customer AC No.: ", self.ac_no)

class Account(Customer):
    def __init__(self, name, iden, ac_no, account_type, balance):
        super().__init__(name, iden, ac_no)
        self.account_type = account_type
        self.balance = balance
    
    def deposit(self):
        amount = int(input("Please enter the amount: "))

        if amount < 100:
            raise ValueError("Amount can't be less than 100")
        self.balance += amount
        print("deposit successfully")
    def withdraw(self):
        amount = int(input("Please enter the amount you want to withdraw: "))

        if amount > self.balance:
            print("Please recharge your wallet:")
            self.deposit()
            return
        
        self.balance -= amount
        print("withdraw successfully")
    def check_balance(self):
        print("Current Balance:", self.balance)



customer_name = input("Enter Customer Name: ")
customer_id = input("Enter Customer ID: ")
customer_account_no = input("Enter Customer Account No: ")

account = Account(customer_name, customer_id, customer_account_no, 'saving', 100)
account.display()

account.check_balance()

account.withdraw()

account.check_balance()

account.deposit()

account.check_balance()