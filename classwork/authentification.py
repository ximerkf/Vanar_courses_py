# APP < user : login

logins = ["administrator","manager","user"]

login = input("Enter your login: ")

if login in logins:
    print("Welcome!")
else:
    print("Access denied!")