# utils.py
def person_data():
    nombre = input("Enter the person's name:")
    numerodecuenta = int(input("Enter a 4-digit account number:"))
    saldoinicial = float(input("Enter the initial balance:"))
person = ()
account = BankAccount(numerodecuenta, saldoinicial)
person.accounts.append(account)
pregunta = input("Are you done adding accounts? (yes/no): ")
if pregunta == "yes":
    break