import secrets
import string
import gmpy2
import inflect
p = inflect.engine()

def main():
    generator()

def generator():

    while True:
        #take input what should the pasword have (letters, numbers, special characters)
        try:
            menu()
            user_choice = int(input("Choose how your password should be generated "))
            if 0 < user_choice < 4:
                while True:
                    try:
                        lenght = int(input("What lenght of pasword would you like? "))
                        if 7 > lenght:
                            print("Password should have at least 8 characters to be minimaly safe, however you should consider more characters ;)")
                        elif lenght > 100:
                            print("Your password should be secure enought with 25 characters, no need to use that many!")
                        else:
                            break
                    except ValueError:
                        print("Password lenght accepts only integers!")
                p_gen(user_choice,lenght)
            elif user_choice == 4:
                break
            else:
                print("\nYour input should be between 1-4\n")
                continue
        except ValueError:
            print("Your input should be between 1-4")
        except EOFError:
            print()
            break



def p_gen(user_choice,lenght):
    inpenetrable = 0
    paswd, strenght = pass_generator_main(user_choice,lenght)
    print(f"\nYour is pasword is: {paswd}\n")

    if strenght < 1:
        days = round((strenght * 12)* 30.44)
        print(f"If attacker is using brute force to enumerate password with speed of 1 bilion requests per second your password will be broken in {days} days\n")
    elif strenght == 1:
        print(f"If attacker is using brute force to enumerate password with speed of 1 bilion requests per second your password will be broken in one year\n")
    else:
        try:
            word = p.number_to_words(int(strenght))
            words = word.split(",")[0]
            print(f"If attacker is using brute force to enumerate password with speed of 1 bilion requests per second your password will be broken in {words} years\n")
        except inflect.NumOutOfRangeError:
            print(f"attacker will need at least quattrodecillion(this is a number with 45 zeros!) years to break you password!\n")
            inpenetrable = 1

    if strenght < 0.5:
        print("This means your password is low security :(\n")
    elif 0.5 < strenght < 1:
        print("This means your password is secure!\n")
    elif strenght > 1 and inpenetrable == 0:
        print("This means your password is indeed very secure!\n")
    else:
        print("Your password is inpenetrable!\n")

    return paswd

def pass_generator_main(user_choice,lenght):
    #generate password
    low_set = string.ascii_letters
    middle_set = string.ascii_letters + string.digits
    high_set = string.ascii_letters + string.digits + string.punctuation

    if user_choice == 1:
        password = "".join(secrets.choice(low_set) for _ in range(lenght))
        p_strenght = gmpy2.mpz(52) ** lenght

    elif user_choice == 2:
        password = "".join(secrets.choice(middle_set) for _ in range(lenght))
        p_strenght = gmpy2.mpz(62) ** lenght

    else:
        password = "".join(secrets.choice(high_set) for char in range(lenght))
        p_strenght = gmpy2.mpz(94) ** lenght

    requests_per_second = 1_000_000_000
    seconds_per_year = 60 * 60 * 24 * 365
    requests_per_year = requests_per_second * seconds_per_year

    years = p_strenght / requests_per_year

    return(password, years)

def menu():
    print("1. Only lower and uppercase letters (low security)")
    print("2. Letters with numbers (good enought for most uses)")
    print("3. Letters, numbers and special characters(most secure!)")
    print("4. Back to menu before")

if __name__ == "__main__":
    main()