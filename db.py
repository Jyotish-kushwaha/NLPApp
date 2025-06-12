import json
class Database:
   def insert(self, name, email, password):
    with open('user.json', 'r') as rf:
        users = json.load(rf)

    if email in users:
        return 0  # Email already exists
    else:
        users[email] = {'name': name, 'password': password}
        with open('user.json', 'w') as wf:
            json.dump(users, wf, indent=4)
        return 1  # Registration successful

        
   def login(self, email, password):
     with open('user.json', 'r') as rf:
        users = json.load(rf)

     user = users.get(email)
     if user and user['password'] == password:
        return 1
     return 0
