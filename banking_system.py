# parent class user
# holds detials about a User 
# has a function to show user data 
# child class Bank
# stroes details about the account balance
# stroes details about the amount 
# allows for deposits ,withdraw ,view_balance

class User:
    def __init__(self,name,age,gender,balance = 0):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance
    def show_details(self):
        return f' Personal Details \n  Name : {self.name} \n  Age : {self.age} \n  Gender : {self.gender}'
    
class BankAccount(User):
    def __init__(self,name,age,gender,account_number):
        super().__init__(name,age,gender,account_number)
        self.balance = 0 
        self.account_number = account_number
    def deposits(self,amount):
      
        if amount > 0 :
            self.balance += amount
        else:
            print('Amount should be positive')
    def withdraw(self,amount):
        if not amount > 0 :
            return 'amount should be positive'
        elif amount < self.balance:
            self.balance -= amount
        else:
            return 'Insufficeint amount'
    def view_balance(self):
        return f'your current balance is : {self.balance}'
    
user1 = BankAccount('kehali',19,'Male')
user1.deposits(500)
print(user1.view_balance())
