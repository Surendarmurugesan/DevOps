from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
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
            # rstrip() = Will strip off the carriage from our line
            user, passw = data.split("|")
            ## split the value based on "|" symbol. Ex: Suren|123, it split into user = Suren , passw = 123.
            print("User: ", user, "Password: ", fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input ('Password: ')

    # file = open('password.txt', 'a')
    # file.close()       --> If we using "file" keyword, add a more step to close the file. otherwise we use "with" keyword, automatically close the file.
    # Below open the file called "passwords.txt"
    # w = write (create new file or override(clear the old data) the file if already exist)
    # r = read (only read mode, can't write/delete anything)
    # a = append (this one is best...read entire file & create a file if not exist, Already exist it will the content at end of the file)
    # Used "as f:" rename the entire function, we can easily call as f.
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add), Press q to Quit? ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue