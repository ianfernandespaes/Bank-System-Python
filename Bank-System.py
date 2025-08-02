menu = """

[1] Deposit
[2] Withdraw
[3] Statement
[0] Exit

Your choice: """

balance = 0
limit = 500
statement = ""
withdraw_count = 0
WITHDRAW_LIMIT = 3

while True:

    option = input(menu)

    if option == "1":
        amount = float(input("Enter the deposit amount: "))

        if amount > 0:
            balance += amount
            statement += f"Deposit: $ {amount:.2f}\n"
        else:
            print("Operation failed! The entered amount is invalid.")

    elif option == "2":
        amount = float(input("Enter the withdrawal amount: "))

        exceeded_balance = amount > balance
        exceeded_limit = amount > limit
        exceeded_withdrawals = withdraw_count >= WITHDRAW_LIMIT

        if exceeded_balance:
            print("Operation failed! You do not have sufficient balance.")
        elif exceeded_limit:
            print("Operation failed! The withdrawal amount exceeds the limit.")
        elif exceeded_withdrawals:
            print("Operation failed! Maximum number of withdrawals exceeded.")
        elif amount > 0:
            balance -= amount
            statement += f"Withdrawal: $ {amount:.2f}\n"
            withdraw_count += 1
        else:
            print("Operation failed! Enter a valid amount.")

    elif option == "3":
        print("\n================ STATEMENT ================")
        print("No deposits or withdrawals were made." if not statement else statement)
        print(f"\nYour Balance: $ {balance:.2f}")
        print("===========================================")

    elif option == "0":
        print("-=" * 9)
        print('Have a great day!')
        print("-=" * 9)
        break

    else:
        print("Invalid operation, please select a valid option.")
