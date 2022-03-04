# Program to check input
# type in Python
import validators
import sys


def menu():
    print("###### Validadores #######")
    option = int(input("1 - Identificador\n2 - Email \n3 - Password \n4 - Idade para trabalho \n5 - Encerrar o "
                       "programa\n"))
    while True:
        if option == 0:
            menu()
        elif option == 1:
            view_identifier()
        elif option == 2:
            view_email()
        elif option == 3:
            view_password()
        elif option == 4:
            view_age_to_work()
        elif option == 5:
            break
            #sys.exit()
        else:
            print("Opção inválida. Tente novamente com: ")
            menu()


def view_identifier():
    identified = input("Entre com um identificador: ")
    validators.check_valid_identifier(identified)
    menu()


def view_email():
    email = input("Entre com um email: ")
    validators.check_email(email)
    menu()


def view_password():
    password = input("Entre com um password: ")
    validators.check_password(password)
    menu()


def view_age_to_work():
    age = int(input("Entre com uma idade: "))
    validators.check_age_for_work(age)
    menu()


if __name__ == "__main__":
    menu()
