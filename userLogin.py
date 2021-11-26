import json

filename = 'database.json'
print("""
to register -> 1
to login -> 2
""")
try:
    choice = int(input("Enter -> "))

    def register(data):
        flag = True
        with open("database.json", 'r') as file:
            db = json.load(file)
            for user in db:
                if user["email"] == data["email"]:
                    flag = False
                    break

            if flag:
                db.append(data)
                with open("database.json", 'w') as file:
                    json.dump(db, file, indent=4)
                return {"status":"ok"}
            else:
                print("Email is already registered..")
                return {"status":"error"}

    def login(email, password):
        registered = False
        with open("database.json", 'r') as file:
            db = json.load(file)
            for user in db:
                if user["email"] == email and user["password"] == password:
                    registered = True
                    print("Login successful. Hello, %s!" %user["name"])
                    break
        if not registered:
            print("You are not registered yet.")

    if choice == 1:
        name = input("Enter your name: ")
        email = input("Enter a valid email: ")
        phone = input("Enter your phone: ")
        password = input("Create a password: ")

        regData = {
            "name": name,
            "email": email,
            "phone": phone,
            "password": password
        }
        print(register(regData))

    elif choice ==2:
        email = input("Email: ")
        password = input("Password: ")
        login(email, password)

    else:
        print("Invalid input.")
except Exception as e:
    print("error occured: ",e)
