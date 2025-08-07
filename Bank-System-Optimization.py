def menu():
    menu = (
        "========== MENU ==========\n"
        "[1] Deposit\n"
        "[2] Withdraw\n"
        "[3] Statement\n"
        "[4] New account\n"
        "[5] List accounts\n"
        "[6] New user\n"
        "[0] Exit\n"
        "Choose an option: "
    )
    return input(menu)

def deposit(balance, amount, statement, /):
    if amount > 0:
        balance += amount
        statement += f"Deposit: $ {amount:.2f}\n"
        print("Deposit successful!")
    else:
        print("Operation failed! Invalid amount.")
    return balance, statement

def withdraw(*, balance, amount, statement, limit, withdrawal_count, withdrawal_limit):
    exceeded_balance = amount > balance
    exceeded_limit = amount > limit
    exceeded_withdrawals = withdrawal_count >= withdrawal_limit

    if exceeded_balance:
        print("Operation failed! Insufficient balance.")
    elif exceeded_limit:
        print("Operation failed! Amount exceeds withdrawal limit.")
    elif exceeded_withdrawals:
        print("Operation failed! Withdrawal limit reached.")
    elif amount > 0:
        balance -= amount
        statement += f"Withdrawal: $ {amount:.2f}\n"
        withdrawal_count += 1
        print("Withdrawal successful!")
    else:
        print("Operation failed! Invalid amount.")

    return balance, statement

def show_statement(balance, /, *, statement):
    print("\n------ STATEMENT ------")
    print("No transactions." if not statement else statement)
    print(f"Balance: $ {balance:.2f}")
    print("-----------------------")

def create_user(users):
    cpf = input("Enter CPF (numbers only): ")
    user = find_user(cpf, users)

    if user:
        print("User with this CPF already exists.")
        return

    name = input("Enter full name: ")
    birth_date = input("Birth date (dd-mm-yyyy): ")
    address = input("Address (street, number - neighborhood - city/state): ")

    users.append({
        "name": name,
        "birth_date": birth_date,
        "cpf": cpf,
        "address": address
    })

    print("User created successfully!")

def find_user(cpf, users):
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None

def create_account(branch, account_number, users):
    cpf = input("Enter the user's CPF: ")
    user = find_user(cpf, users)

    if user:
        print("Account created successfully!")
        return {"branch": branch, "account_number": account_number, "user": user}

    print("User not found. Account creation canceled.")

def list_accounts(accounts):
    for account in accounts:
        print("------------------------------")
        print(f"Branch: {account['branch']}")
        print(f"Account: {account['account_number']}")
        print(f"Holder: {account['user']['name']}")
        print("------------------------------")

def main():
    WITHDRAWAL_LIMIT = 3
    BRANCH = "0001"

    balance = 0
    limit = 500
    statement = ""
    withdrawal_count = 0
    users = []
    accounts = []

    while True:
        option = menu()

        if option == "1":
            amount = float(input("Deposit amount: "))
            balance, statement = deposit(balance, amount, statement)

        elif option == "2":
            amount = float(input("Withdrawal amount: "))
            balance, statement = withdraw(
                balance=balance,
                amount=amount,
                statement=statement,
                limit=limit,
                withdrawal_count=withdrawal_count,
                withdrawal_limit=WITHDRAWAL_LIMIT
            )

        elif option == "3":
            show_statement(balance, statement=statement)

        elif option == "4":
            account_number = len(accounts) + 1
            account = create_account(BRANCH, account_number, users)
            if account:
                accounts.append(account)

        elif option == "5":
            list_accounts(accounts)

        elif option == "6":
            create_user(users)

        elif option == "0":
            print("Exiting the system. Thank you!")
            break

        else:
            print("Invalid option. Please try again.")

main()
