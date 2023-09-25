import string
import gmpy2
import inflect
import re
p = inflect.engine()

def main():
    p_check()

def p_check():
    while True:
        try:
            menu()
            user_choice = int(input("Choice "))
            if user_choice == 1:
                password = input("Password: ")
                #deufalt speed
                speed = 1_000_000_000
                continue
            elif user_choice == 2:
                #deufalt speed
                print("Remember lower the request per second the harder it is to bruteforce password")
                speed = int(input("Requests per second: "))
                continue
            elif user_choice == 3:
                check(password, speed)
            elif user_choice == 4:
                break
            else:
                raise ValueError
        except ValueError:
            print("Your input should be between 1-4")

        except UnboundLocalError:
            print("You have to first set a password you want to check!")

        except EOFError:
            print()
            break

def check(password, speed):
    inpenetrable = 0
    v, t, l, s, fileintxt = pas_check(password, speed)
    print()

    #password strenght
    sec_peryear = 60 * 60 * 24 * 365
    req_per_year = s * sec_peryear

    p_strenght = gmpy2.mpz(v) ** l
    strenght = p_strenght / req_per_year

    #telling user what password have
    characters =p.join(t)
    print(f"Your password has {characters}!\n")

    #printing message to user
    if fileintxt == 1:
         print("Your password is very common, change it immediately!\n")

    else:
        if strenght < 1:
            days = round((strenght * 12)* 30.44)
            if days < 1:
                print("Attacker will enumerate password in lest than a day! :(\n")
            else:
                print(f"Attacker will enumerate password in {days} days\n")
        elif strenght == 1:
            print(f"Attacker will enumerate password in one year\n")
        else:
            try:
                word = p.number_to_words(int(strenght))
                words = word.split(",")[0]
                print(f"Attacker will enumerate password in {words} years\n")
            except inflect.NumOutOfRangeError:
                print(f"Attacker will need at least quattrodecillion(this is a number with 45 zeros!) years to break you password!\n")
                inpenetrable = 1

        if strenght < 0.5:
            print("This means your password is low security :(\n")

        elif 0.5 < strenght < 1:
            print("This means your password is secure!\n")
        elif strenght > 1 and inpenetrable == 0:
            print("This means your password is indeed very secure!\n")
        else:
            print("Your password is inpenetrable!\n")


def pas_check(password, speed):

    digit = re.search(r"\d", password)
    low_a = re.search(r"[a-z]", password)
    upp_A = re.search(r"[A-Z]", password)
    special = re.search("[" + re.escape(string.punctuation) + "]", password)

    value = 0
    tell = []
    lenght = len(password)

    if digit:
        value += 10
        tell.append("digits")
    if low_a:
        value += 26
        tell.append("lowercase")
    if upp_A:
        value += 26
        tell.append("uppercase")
    if special:
        value += 32
        tell.append("special characters")

    found = 0
    with open("common.txt") as file:
        infile = file.read().splitlines()
        for row in infile:
            if matches := re.findall(row, password, re.IGNORECASE):
                found = 1


    return value,tell,lenght,speed,found



def menu():
    print("1. What is the password ")
    print("2. Set attack speed(deufalt is set to 1 billion per second)")
    print("3. Run Password Check")
    print("4. Back to menu before")


if __name__ == "__main__":
    main()