from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def main():
    encrypt()
    decrypt()


def encrypt():
    key = RSA.generate(2048)

    #creating keys
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    #saving keys
    with open("private_key.pem", 'wb') as file:
        file.write(private_key)

    with open("public_key.pem", 'wb') as file:
        file.write(public_key)

    #user input
    u_inp = input("Enter the message you want to encrypt: ")

    #encryption
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted = cipher.encrypt(u_inp.encode())
    print("Encrypted Message:")
    print(encrypted.hex() + "\n")

def decrypt():
    #opening private key pem
    private_key_file = "private_key.pem"
    with open(private_key_file, 'rb') as file:
        private_key_data = file.read()

    #user input and converting from hex
    encrypted_message_hex = input("Enter the hex-encoded encrypted message: ")
    encrypted_message = bytes.fromhex(encrypted_message_hex)

    #decryption
    rsa_key = RSA.import_key(private_key_data)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    print("Decrypted Message:")
    print(decrypted_message.decode() + "\n")

if __name__ == "__main__":
   main()
