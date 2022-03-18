from cryptography.fernet import Fernet
# Reference for using Fernet encryption and decryption:
# https://cryptography.io/en/latest/fernet/

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# note: write_key only needs to be called once to create a .key file
write_key()


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "\nWhat would you like to do?\n[1] Add new password\n[2] View existing password \n[4] Exit\n")#.lower()
    if mode == "3":
        break

    if mode == "2":
        view()
    elif mode == "1":
        add()
    else:
        print("Invalid mode.")
        continue
