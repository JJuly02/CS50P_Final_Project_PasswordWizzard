# Password Wizard: A Multi-Tool for Password Management and Encryption

Welcome to **Password Wizard**, a versatile tool that demonstrates key concepts in password management, encryption, and cybersecurity. This project offers five unique subprograms that help users understand and interact with password-related tools, ranging from brute force demonstrations to password generation and encryption.

---

## 📂 File Structure

Here’s an overview of the files in this repository:

- **`brute.py`**: Simulates a brute-force attack on passwords.
- **`check.py`**: Evaluates the strength of user-provided passwords.
- **`generator.py`**: Generates secure passwords based on user specifications.
- **`hasher.py`**: Provides hashing and encryption/decryption functionalities.
- **`expired.py`**: Manages password expiration and highlights outdated passwords.
- **`project.py`**: The main program that ties all subprograms together.
- **`test_project.py`**: Unit tests for the project.
- **`common.txt`**: A list of common passwords for security checks.
- **`pass.csv`**: Stores plaintext passwords (for demo purposes only).
- **`private_key.pem`** & **`public_key.pem`**: RSA keys used in encryption and decryption.
- **`requirements.txt`**: Lists dependencies for the project.

---

## 🎯 Features

### **1. Brute Force Simulation**
- Simulates how a brute-force attack works.
- Allows users to:
  - Set parameters for the attack (e.g., character set).
  - Test a default password or specify their own.
- Shows the time and effort required for a brute-force attack.

---

### **2. Password Strength Checker**
- Checks the strength of user-provided passwords.
- Features:
  - Simulates cracking speed (default: 1 billion tries/second, customizable).
  - Checks if the password exists in the `common.txt` list of weak passwords.
  - Recommends changing insecure passwords.

---

### **3. Password Generator**
- Creates strong, random passwords.
- Allows users to:
  - Specify characters (e.g., letters, numbers, symbols).
  - Define the desired password length.
- Evaluates and displays the security level of generated passwords.

---

### **4. Encryption Tool**
- Offers three modes of encryption:
  1. **Hashing:** Hashes input using a user-selected algorithm and outputs the raw and hex values.
  2. **Asymmetric Encryption:** Encrypts and decrypts data using RSA public/private key pairs.
  3. **Symmetric Encryption:** Encrypts and decrypts data with a user-provided key.

---

### **5. Password Manager (Demo)**
- Demonstrates how password managers work:
  - Stores and retrieves plaintext passwords (for educational purposes only).
  - Checks if a password should be updated based on when it was added.
- **Note:** Passwords are stored in plaintext in this demo. Real-world applications should use secure encryption for storage.

---

## 🚀 How to Use

### Prerequisites
- Python 3.8+ installed.
- Install dependencies:
  ```bash
  pip install -r requirements.txt
