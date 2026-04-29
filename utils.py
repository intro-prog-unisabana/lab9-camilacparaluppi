# utils.py
from bank_account import BankAccount
from person import Person
def person_data():
    nombre = input("Enter the person's name: ")
    person = Person(nombre)
    while True:
        numerodecuenta = int(input("Enter a 4-digit account number: "))
        saldoinicial = float(input("Enter the initial balance: "))
        account = BankAccount(numerodecuenta, saldoinicial)
        person.accounts.append(account)
        pregunta = input("Are you done adding accounts? (yes/no): ")
        if pregunta == "yes":
            break
    return person
def balance_summary(person_list):
    for person in person_list:
        total = 0
        for account in person.accounts:
            total += account.balance

        print(f"{person.name} : {total:.2f}")