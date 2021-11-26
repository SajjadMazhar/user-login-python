import json, os

filename = 'database.json'
if not os.path.exists("database.json"):
    with open("database.json", "w") as f:
        init_data = []
        json.dump(init_data, f, indent=4)

print("""
to register -> 1
to login -> 2
to update data -> 3
to delete data -> 4
""")


choice = int(input("Enter -> "))

def spChar(string):
    for char in string:
        if char in ['@','_', '!','&','$']:
            return True
    return False

def upperChar(string):
    for char in string:
        if char.isupper():
            return True
    return False

def lowerChar(string):
    for char in string:
        if char.islower():
            return True
    return False
    

def dataInputs():
    valid_name = False
    valid_email = False
    valid_phone = False
    valid_pass = False
    while not valid_name:
        name = input("Enter your name: ")
        if len(name) >= 3:
            valid_name = True
        else:
            print("name must be of 3 or more characters")
            continue
    while not valid_email:
        email = input("Enter a valid email: ")
        if 'gmail.com' in email:
            valid_email = True
        else:
            print("You entered an invalid email!")
            continue
    while not valid_phone:
        phone = int(input("Enter your phone: "))
        if len(str(phone)) >= 10:
            valid_phone = True
        else:
            print("Enter a valid phone number!")
            continue
    while not valid_pass:
        password = input("Create a password: ")
        if len(password)>=8 and spChar(password) and upperChar(password) and lowerChar(password):
            valid_pass = True
        else:
            print("Password must have 8 or more characters and contain atleast one capital letter,  one lower character, one number and a special character eg. (@, $, &, _, !)")
            continue
    return [name, email, phone, password]

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

def updateData(email):
    try:
        with open("database.json", 'r') as file:
            db = json.load(file)
            for user in db:
                if user["email"] == email:
                    print("***update***")
                    uname = input("Update Name: ")
                    uemail = input("Update Email: ")
                    uphone = int(input("Updata Phone: "))
                    upassword = input("Update Password: ")
                    updatedJson = {
                        "name": uname,
                        "email": uemail,
                        "phone": uphone,
                        "password": upassword
                    }
                    db.append(updatedJson)
                    with open("database.json", 'w') as file:
                        json.dump(db, file, indent=4)
                    deleteData(email)
                    break
        return {'status':"ok"}
    except Exception as e:
        print({"status":f"Error: {e}"})

def deleteData(email):
    try:
        with open("database.json", 'r') as file:
            db = json.load(file)
            for user in db:
                if user["email"] == email:
                    db.remove(user)
                    break
            with open("database.json", 'w') as file:
                json.dump(db, file, indent=4)
        return {"status":"ok"}
    except Exception as e:
        return e
if choice == 1:
    
    inputs = dataInputs()
    regData = {
        "name": inputs[0],
        "email": inputs[1],
        "phone": inputs[2],
        "password": inputs[3]
    }
    print(register(regData))

elif choice ==2:
    email = input("Email: ")
    password = input("Password: ")
    login(email, password)
elif choice == 3:
    email = input("Enter Email: ")
    print(updateData(email))
elif choice == 4:
    email = input("Enter Email: ")
    print(deleteData(email))
else:
    print("Invalid input.")
