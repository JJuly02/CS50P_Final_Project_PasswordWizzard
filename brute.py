import random
import string
import time
import pyfiglet

def main():
    b_force()

def b_force():
    #deufalt settings
    password = "pass"
    letters = False
    numbers = False
    special = False
    page()
    print("In this exercise you can see at hand how does the brute force attack realy works. You are welcom to change anny settings you want and also change the deufalt password which for the simplicity is 'pass'.\n")
    #main loop
    while True:
        try:
            menu()
            user_choice = int(input("Choice: "))
            if user_choice == 1:
                letters = ispositive("Does password have upper letters? ")
                numbers = ispositive("Does password have numbers? ")
                special = ispositive("Does password have special characters? ")
            elif user_choice == 2:
                lenght = len(password)
                t1 = time.time()
                asw = bruteforce(letters, numbers, special, lenght, password)
                if asw == True:
                    t2 = time.time()
                    T = t2 - t1
                    print(f"password is '{password}' and it was broken in {T} seconds!")
            elif user_choice == 3:
                password = input("What should be new password? ")
            elif user_choice == 4:
                break
            else:
                raise ValueError
        except ValueError:
            print("Your input should be betwen 1-4")
        except EOFError:
            print()
            break

def bruteforce(letters, numbers, special, lenght, password):
    characters = list(string.ascii_lowercase)

    if letters == True:
        characters = list(string.ascii_letters)
    if numbers == True:
        characters += list(string.digits)
    if special == True:
        characters += list(string.punctuation)



    while True:
        word = []
        for i in range(lenght):
            i = random.choice(characters)
            word.append(i)
        result = "".join(word)
        print(result)
        if result == password:
            break

    return True


def page():
    website_text = pyfiglet.figlet_format("Website", font="big")

    login_prompt = "Username: Admin\nPassword: ________\n"

    # Calculate the width of the terminal
    terminal_width = 80

    # Center-align the text
    website_lines = website_text.splitlines()
    formatted_website = "\n".join(line.center(terminal_width) for line in website_lines)

    # Combine the formatted text with the login prompt
    login_page = f"{formatted_website}\n{login_prompt}"

    # Print the login page
    print(login_page)

def menu():
    print("1. Set parameters")
    print("2. Run bruteforce attack")
    print("3. Set new admin password")
    print("4. Back to menu before")

def ispositive(prompt):
    yes = "yes"
    no = "no"
    while True:
        try:
            annswer = input(prompt)
            if annswer.lower() == yes:
                return True
            elif annswer.lower() == no:
                return False
            else:
                raise ValueError
        except ValueError:
            print("Usage: 'yes' / 'no'")

if __name__ == "__main__":
    main()