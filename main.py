from bank_account import BankAccount
from person import Person
from utils import person_data, balance_summary
def main():
    people = []  # List to store all Person objects

    while True:
        # Display menu
        print("Choose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")

        choice = input().strip()

        # Option 1: Add a new person
        if choice == "1":
            person = person_data()
            people.append(person)

        # Option 2: Add an account to an existing person
        elif choice == "2":
            nombre = input("Enter the person's name: ")
            found = False
            for person in people:
                if person.name == nombre:
                    numerodecuenta = int(input("Enter a 4-digit account number: "))
                    saldoinicial = float(input("Enter the initial balance: "))
                    account = BankAccount(numerodecuenta, saldoinicial)
                    person.add_account(account)
                    found = True
                    break
            if found == False:  
                print("Person not found.")

        # Option 3: Show all balances
        elif choice == "3":
            if len(people) == 0:
                print("No data to show.")
            else:
                balance_summary(people)

        # Option 4: Quit
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()
