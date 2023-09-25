import hashlib
from cryptography.fernet import Fernet


def main():
    p_hash()

def p_hash():
    while True:
        try:
            menu()
            user_choice = int(input("Choice "))
            if user_choice == 1:
                user_input = input("Input: ")
                aname = menu_hash()
                hashe(user_input, aname)
            elif user_choice == 2:
                RSA()
            elif user_choice == 3:
                user_key()
            elif user_choice == 4:
                break
            else:
                raise ValueError
        except ValueError:
            print("Your input should be between 1-4")
        except EOFError:
            print()
            break

def hashe(u_inp, aname):

    #hashing
    h = hashlib.new(aname)
    h.update(u_inp.encode())
    print(f"\nRaw: {h.digest()}")
    print(f"Hex: {h.hexdigest()}\n")

#-------RSA public and private-----
def RSA():
    while True:
        try:
            menu_decrypt_encrypt()
            user_input = int(input("Choice "))
            if user_input == 1:
                encrypt_rsa()
            elif user_input == 2:
                decrypt_rsa()
            elif user_input == 3:
                break
            else:
                raise ValueError
        except KeyError:
            print("This text is not encrypted or the key is wrong")
        except ValueError:
            print("Your input shuld be betwen 1-3")
        except EOFError:
            print()
            break

def encrypt_rsa():
    from rsa_encrypt.rsa_dencrypt import encrypt
    encrypt()

def decrypt_rsa():
    from rsa_encrypt.rsa_dencrypt import decrypt
    decrypt()

#--------User inpu key------------
def user_key():
    while True:
        try:
            menu_decrypt_encrypt()
            user_input = int(input("Choice "))
            if user_input == 1:
                encrypt_user_key()
            elif user_input == 2:
                decrypt_user_key()
            elif user_input == 3:
                break
            else:
                raise ValueError
        except ValueError:
            print("Your input shuld be betwen 1-2")
        except KeyError:
            print("This text is not encrypted or the key is wrong")
        except EOFError:
            break

#encrypt
def encrypt_user_key():
    from user_encrypt.decrypt_encrypt import encrypt_word
    encrypted_word = encrypt_word()
    print(f"Encrypted {encrypted_word}")

#decrypt
def decrypt_user_key():
    from user_encrypt.decrypt_encrypt import decrypt_word
    decrypted_word = decrypt_word()
    print(f"Decrypted: {decrypted_word}")

def menu():
    print("1. Hash")
    print("2. Encrypt & Decrypt with Public and Private key")
    print("3. Encrypt & Decrypt with your own key")
    print("4. Back to menu before")

def menu_hash():
    i = 1
    h_alg = {
    1: 'md5',
    2: 'sha1',
    3: 'sha224',
    4: 'sha256',
    5: 'sha384',
    6: 'sha512',
    7: 'blake2b',
    8: 'blake2s',
    9: 'sha3_224',
    10: 'sha3_256',
    11: 'sha3_384',
    12: 'sha3_512',
    }

    print("Chose algoritm: ")
    for number, name in h_alg.items():
        print(f"{number}. {name}")
        i += 1

    while True:
        try:
            h_name = int(input("Choice "))
            if h_name in range(i):
                aname = h_alg[h_name]
                return aname
            else:
                raise ValueError

        except (ValueError,KeyError):
            print("Chose hash algoritm from the list")

def menu_decrypt_encrypt():
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Back to menu")

if __name__ == "__main__":
    main()