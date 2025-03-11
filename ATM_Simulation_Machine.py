import time 

# ATM class created to contain all the required functions of a ATM
class ATM:
    def __init__ (self, pin, balance = 0):  # Initializing an ATM object
        self.pin = pin
        self.balance = balance
        self.transaction_history = [] 
      
    def check_balance(self):  # Function for user to check their balance
        print(f"Your current balance is: Rs.{self.balance}")
        self.transaction_history.append("Balance inquiry")
      
    def deposit(self, amount):  # Function for user to deposit a certain amount into their account
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: Rs.{amount}")
            print(f"Successfully deposited Rs.{amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")
          
    def withdraw(self, amount):  # Function for user to withdraw money from their account
        if 0 < amount <=self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: Rs.{amount}")
            print(f"Successfully withdrew Rs.{amount}. Remaining balance: Rs.{self.balance}")
        else:
            print("Insufficient balance or invalid amount.")
            
    def change_pin(self, old_pin):  # Function for user to change their ATM pin
        if old_pin == self.pin:
            new_pin = input("Enter the new PIN: ")
            confirm_pin = input("Confirm the new PIN: ")
            if confirm_pin == new_pin:
                self.pin = new_pin
                self.transaction_history.append("PIN changed")
                print("PIN successfully changed.")
            else: 
                print("PINs don't match. PIN change failed.")
        else: 
            print("Incorrect PIN. PIN change failed.")
            
    def show_transaction_history(self):  # Function for user to view their transaction history
        print("--------------------------------------------")
        print("Transaction History: ")
        for transaction in self.transaction_history:
            print("\t", transaction)
        print("---------------------------------------------")

            
def main():  #MAIN function
    atm = ATM(pin="1234", balance=5000)
    while True:
        print("\nATM Options: ")
        print("1. Check Balance \n2. Deposit Cash \n3. Withdraw Cash \n4. Change PIN \n5. View Transaction History \n6. Exit")
        print("P.S.: Default PIN = 1234, Default balance = 5000")
        choice = input("Enter a choice: ")
        
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            old_pin = input("Enter current PIN: ")
            atm.change_pin(old_pin)
        elif choice == '5':
            atm.show_transaction_history()
        elif choice == '6':
            print("Thank you for using our ATM. Have a good day~")
            exit()
        else: 
            print("Invalid choice! Please try again.")
        time.sleep(2)  # A small pause before the next iteration of while loop
            
try:
    main()
except KeyboardInterrupt or ValueError:
    print("You either entered an invalid value or tried to stop the program.......Goodbye~")
    
