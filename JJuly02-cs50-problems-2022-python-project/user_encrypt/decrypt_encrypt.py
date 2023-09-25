import operator

def main():
    encrypted_word = encrypt_word()
    print(f"Encrypted {encrypted_word}")

    decrypted_word = decrypt_word()
    print(f"Decrypted: {decrypted_word}")

#encryption
def encrypt_word():
    goal = "encrypt"
    uword = input("Word to encrypt: ")
    ukey = input("User key: ")
    operation = "add"
    return nested_crypting(uword, ukey, operation, goal)


#decryption
def decrypt_word():
    goal = "decrypt"
    uword = input("Word to decrypt: ")
    ukey = input("User key: ")
    operation = "subtract"
    return nested_crypting(uword, ukey, operation, goal)


def nested_crypting(uword, ukey, operation, goal):
     #when key and input are the same lenght or key is longer
    if len(uword) <= len(ukey):
        encrypted_word = []
        #changing u_input to ascii list and adding them together
        for char, key_char in zip(uword, ukey):
            if goal == "encrypt":
                encrypted_char = ord(char) + (2 * ord(key_char))
            else:
                encrypted_char = ord(char) - (2 * ord(key_char))
            encrypted_word.append(encrypted_char)
        try:
            return ''.join(map(chr, encrypted_word))
        except ValueError:
            raise KeyError
    else:
        try:
            uwords = []
            ukeys = []
            for i in uword:
                uwords.append(ord(i))
            for j in ukey:
                ukeys.append(ord(j))
            encrypted_word = enc_calculator(uwords, ukeys, operation)
            encrypted = ""
            for num in encrypted_word:
                encrypted += chr(num)

            return encrypted
        except ValueError:
            raise KeyError


#calculator that extends key by itself and then chosing operation
def enc_calculator(first, second, operation):

    second = [x * 2 for x in second]
    second *= len(second)


    if operation == "add":
        return [x + y for x, y in zip(first, second)]
    elif operation == "subtract":
        return [x - y for x, y in zip(first, second)]


if __name__ == "__main__":
    main()