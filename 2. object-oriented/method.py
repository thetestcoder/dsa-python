class Customer:
    def __init__(self, name, iden, ac_no) -> None:
        self.name = name
        self.id = iden
        self.ac_no = ac_no
    def display(self):
        print("Customer Name: ", self.name)
        print("Customer ID: ", self.id)
        print("Customer AC No.: ", self.ac_no)

customer_name = input("Enter Customer Name: ")
customer_id = input("Enter Customer ID: ")
customer_account_no = input("Enter Customer Account No: ")

customerObject = Customer(customer_name, customer_id, customer_account_no)
customerObject.display()