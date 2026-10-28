def bank_system():
    print("Welcome!")
    balance = float(input("Enter your balance: "))

    while True:
        print("\nSelect an option:")
        print("1. Withdraw Amount")
        print("2. Deposit Amount")
        print("3. Exit")
        
        choice = input("Option: ")

        if choice == '1':
            print("\nHow much amount you want to withdraw from your account?")
            amount = float(input("Amount: "))
            if amount <= balance:
                balance -= amount
                print(f"Your new balance is: {int(balance) if balance.is_integer() else balance}")
            else:
                print("Insufficient balance!")
                
        elif choice == '2':
            print("\nHow much amount you want to deposit in your account?")
            amount = float(input("Amount: "))
            balance += amount
            print(f"Your new balance is: {int(balance) if balance.is_integer() else balance}")
            
        elif choice == '3':
            print("\nThank you for using the system!")
            break
        else:
            print("Invalid option! Please select 1, 2, or 3.")

if __name__ == "__main__":
    bank_system()