# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:21:38 2026

@author: SANTOSH KUMAR SHARMA
"""


"""
=========================================
      BANK ACCOUNT MANAGEMENT SYSTEM
=========================================

Author  : Santosh Kumar Sharma
Language: Python
Project : Mini Banking System

=========================================
"""
class BankAccount:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"""
                  =========================================
                          DEPOSIT SUCCESSFUL
                  =========================================
                  
                  Account Holder   : {self.name}
                  Deposited Amount : Rs. {amount}
                  
                  Updated Balance  : Rs. {self.balance}
                  
                  =========================================
                  """)
            
        else:
            print("Invalid Deposit Amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Withdrawal Amount")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"""
                  =========================================
                          WITHDRAWAL SUCCESSFUL
                  =========================================
                  
                  Account Holder   : {self.name}
                  Withdrawn Amount : Rs. {amount}
                  
                  Remaining Balance: Rs. {self.balance}
                  
                  =========================================
                  """)

        else:
            print(f"""
                  =========================================
                              TRANSACTION FAILED
                  =========================================
                  
                  Reason : Insufficient Balance
                  
                  Available Balance : Rs. {self.balance}
                  
                  =========================================
                  """)
            
    def transfer(self, other_account, amount): 
        if amount <= self.balance: 
            self.balance -= amount
            other_account.balance += amount
            print(f""" 
                  ===============TRANSFER RECEIPT===============
                  Sender     : {self.name}
                  Receiver   : {other_account.name}
                  Amount     : Rs. {amount}
                  Status     : Successfull
                  
                  Remaining Balance :  Rs. {self.balance}
                  
                  -----------------------------------------
                  Sender Balance    : Rs. {self.balance}
                  Receiver Balance  : Rs. {other_account.balance}
                    
                  =========================================
                  """)

        else:
            print(f"""
                  =========================================
                              TRANSFER FAILED
                  =========================================
                  
                  Reason : Insufficient Balance
                  
                  Available Balance : Rs. {self.balance}
                  
                  =========================================
                  """)
        
    def display(self):
        print(f"""
              =========================================
                          ACCOUNT DETAILS
              =========================================
              
              Account Holder : {self.name}
              Current Balance: Rs. {self.balance}
              
              =========================================
              """)
        
    print("""
=========================================
       CREATE YOUR BANK ACCOUNT
=========================================
""")

name1 = input("Enter First Account Holder Name : ")
balance1 = int(input("Enter Initial Balance : "))

name2 = input("\nEnter Second Account Holder Name : ")
balance2 = int(input("Enter Initial Balance : "))

B1 = BankAccount(name1, balance1)
B2 = BankAccount(name2, balance2)

accounts = {
    B1.name.lower(): B1,
    B2.name.lower(): B2
}

def get_account():

    name = input("Enter Account Holder Name : ").lower()

    if name in accounts:
        return accounts[name]

    else:
        print("Account Not Found")
        return None

# =========================================
#              MAIN MENU
# =========================================

while True:

    print("""
          =========================================
                  BANK MANAGEMENT MENU
          =========================================
          
          1. Deposit Money
          2. Withdraw Money
          3. Transfer Money
          4. Display Account Details
          5. Exit
          
          =========================================
          """)
          
    choice = int(input("Enter Your Choice : "))

    # Deposit
    if choice == 1:
        account = get_account()
        if account:
            amount = int(input("Enter Deposit Amount : "))
            account.deposit(amount)

    # Withdraw
    elif choice == 2: 
        account = get_account()
        if account:
            amount = int(input("Enter Withdrawal Amount : "))
            account.withdraw(amount)

    # Transfer
    elif choice == 3:
        sender_name = input("Enter Sender Name : ").lower()
        receiver_name = input("Enter Receiver Name : ").lower()
    
        if sender_name in accounts and receiver_name in accounts:
            sender = accounts[sender_name]
            receiver = accounts[receiver_name]
            amount = int(input("Enter Transfer Amount : "))
            sender.transfer(receiver, amount)
        else:
            print("Invalid Account Name")

    # Display Details
    elif choice == 4:

        print("\nFIRST ACCOUNT DETAILS")
        B1.display()

        print("\nSECOND ACCOUNT DETAILS")
        B2.display()

    # Exit
    elif choice == 5:

        print("""
=========================================
     THANK YOU FOR USING OUR BANK
=========================================
""")
        break

    # Invalid Choice
    else:

        print("""
=========================================
           INVALID CHOICE
=========================================
Please Enter a Valid Option
=========================================
""")
