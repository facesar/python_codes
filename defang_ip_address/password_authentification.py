import getpass

database = {"cesar.espino": "+79992315462", "espino.cesar": "+79993264879"}
username = input("Enter your Username: ")
password = getpass.getpass("Enter your Password: ")
for i in database.keys():
    if username == i:
        while password != database(i):
            password = getpass.getpass("Enter your Password A gain: ")
        break

print("Verified")