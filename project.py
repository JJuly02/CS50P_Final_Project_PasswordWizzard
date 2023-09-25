import random
import sys
from termcolor import colored
from pyfiglet import Figlet
figlet = Figlet()


def main():
    hello()

    while True:
        try:

            menu()
            user_input = int(input("Choice "))

            if user_input == 1:
                brute_force()

            elif user_input == 2:
                pass_check()

            elif user_input == 3:
                pass_generator()


            elif user_input == 4:
                pass_hasher()

            elif user_input == 5:
                p_expired()

            elif user_input == 6:
                break
            else:
                raise ValueError


        except EOFError:
            break

        except ValueError:
            print("Input should be betwen 1-6")
            continue


    sys.exit("Goodbye!")

#-------------------BRUTE FORCE ATTACEKR-------------------
def brute_force():
    from brute import b_force
    b_force()

#--------------------PASSWORD CHECKER----------------------
def pass_check():
    from check import p_check
    p_check()

#--------------------PASWORD GENERATOR---------------------
def pass_generator():
    from generator import generator
    generator()

#-------------------PASSWORD HASHER&ENCRYPT--------------------------
def pass_hasher():
    from hasher import p_hash
    p_hash()
#-------------------EXPIRED REMINDER-------------------------
def p_expired():
    figlet.setFont(font="larry3d")
    print(figlet.renderText("Password Querry"))
    from expired import expireed
    expireed()

def menu():
    print("\n1. Brute Force Attack")
    print("2. Is my password safe?")
    print("3. Generate safe password")
    print("4. Encryption tool")
    print("5. Mini Password Menager")
    print("6. Exit")

def hello():
    #list of passheders
    header_list = [
    "Password Wizard",
    "Key Master",
    "Secret Getter",
    "Access Guru",
    "Password Maestro",
    "Code Whisperer",
    "Security Sentinel",
    "Itruder Pro",
    "Passcode Enchanter",
    "Password H4K3R"
    ]
    greet = random.choice(header_list)

    #fonts list
    pyfiglet_fonts = [
    "banner",
    "big",
    "block",
    "doom",
    "larry3d",
    "poison",
    "rectangles",
    "alligator2",
    "nancyj"
    ]
    figlet.setFont(font = random.choice(pyfiglet_fonts), width=110)


    #printing password
    print(colored(figlet.renderText(greet), "blue"))
    print("This program is intended solely for educational purposes and should not be used for any commercial, malicious, or unauthorized activities.")


if __name__ == "__main__":
    main()