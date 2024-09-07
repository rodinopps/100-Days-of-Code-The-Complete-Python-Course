'''myUser = {"name": "David", "age": 128}'''

'''myUser = {"name": "David", "age": 128}

print(myUser["name"])

# This code outputs 'David'.'''

'''myUser = {"name": "David", "age": 128}

myUser["name"] = "The legendary David"
print(myUser)

# This code outputs 'name:'the legendary David', 'age':'128.'''

'''myUser = {"name": "David", "age": 128}

print(f"Your name is {myUser['name']} and your age is {myUser['age']}")'''

'''myUser = {"name": "David", "age": 128}

print(myUser["name"])'''

'''myUser = {"name": "David", "age": 128}

print(myUser["name"])'''

'''myUser = {"name":"David", "age": 128}

myUser["age"] = 129

print(myUser)'''

'''myUser = {"name":"Andy", "age":128}

myUser["age"] = 129

print(myUser["name"])'''

'''myUser = {"name": "David", "age": 128}

print(f"Your name is {myUser['name']} and your age is {myUser['age']}")'''

'''myUser = {"name": "David", "age": 128}

print(myUser["name"])'''

'''myUser = {"name":"David", "age": 128}

myUser["age"] = 129

print(myUser)'''

'''myUser = {"name":"Andy", "age":129}

print(myUser["name"])'''


name = input("Enter your name: ").strip().capitalize()
birth = input("Enter your date of birth: ").strip()
number = input("Enter your telephone number: ").strip()
email = input("Enter your email: ")
address = input("Enter your address: ")
info = {"name": name, "birth": birth, "number": number, "email": email, "address": address}

print(f"Hi {name}. Our dictionary says that you were born on {birth}, we can call you on {number}, email {email}, or write to {address}.")