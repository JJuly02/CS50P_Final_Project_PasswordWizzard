import csv
import sys
from datetime import datetime
import inflect
from tabulate import tabulate
from getpass import getpass
p = inflect.engine()

def main():
    expireed()

def expireed():

    while True:
        try:
            menu()
            choice = int(input("Choice "))
            if choice == 1:
                view()
            elif choice == 2:
                view_pass()
            elif choice == 3:
                add()
            elif choice == 4:
                delete()
            elif choice == 5:
                break
            else:
                print("Integeer not in range")
        except ValueError:
            print("Input must be integeer!")
        except EOFError:
            print()
            break

def view():

    with open("pass.csv", "r") as file:
        reader = csv.DictReader(file)
        tbl = [{"Date": row["date"], "Website": row["website"]} for row in reader]

    today = datetime.now().date()

    for row in tbl:
        d = row["Date"]
        date = datetime.strptime(d, "%Y-%m-%d").date()
        diference = (date - today).days
        row["Days since aded password"] = -diference
        row["You should change password in"] = 90 - (-int(diference))

    table = tabulate(tbl, headers="keys",tablefmt="fancy_grid")
    print(table)

def view_pass():
    if master_pass() == True:

        with open("pass.csv", "r") as file:
            reader = csv.DictReader(file)
            tbl = list(reader)

        table = tabulate(tbl, headers="keys",tablefmt="fancy_grid")
        print(table)

def add():
    today = datetime.now().date()
    password = getpass("Password: ")
    website = input("Website: ")
    with open("pass.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "website", "password"])
        writer.writerow({"date": today, "website": website, "password": password})

def delete():
    #show table
    if master_pass() == True:
        i = 0
        tab = []
        with open("pass.csv", "r") as file:
            reader = csv.DictReader(file)
            tab = list(reader)
            for row in tab:
                i += 1
        table = tabulate(tab, headers="keys",tablefmt="fancy_grid", showindex="always")
        print(table)

        while True:
            try:
                user_input = int(input("What row you want to delete? "))
                if user_input in range(i):
                    break
                else:
                    print("Integeer not in range")
            except ValueError:
                print("Input must be integeer!")


        delete_row = tab.pop(user_input)
        with open("pass.csv", "w", newline="") as file:
            fieldnames = ["date", "website", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(tab)

        with open("pass.csv", "r") as file:
            reader = csv.DictReader(file)
            tab = list(reader)

        table = tabulate(tab, headers="keys",tablefmt="fancy_grid", showindex="always")
        print(table)

def menu():
    print("1. View the table for your websites")
    print("2. View the table for your websites with passwords")
    print("3. Add new password")
    print("4. Delete password")
    print("5. Back to menu before")

def master_pass():
    attempts = 0
    while True:
        password = getpass("Master Password: ")
        if password != "Harvard50":
            attempts += 1
            if attempts == 3:
                sys.exit("Wrong password in 3 attempts! Exiting...")
        else:
            return True


if __name__ == "__main__":
    main()