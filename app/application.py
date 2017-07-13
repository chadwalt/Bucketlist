class App:
    users = []                        
        
    ## Login method.
    def login(self, username, password):        
        if (username and password):
            for user in self.users:                
                if (user['username'] == username and user['password'] == password):
                    return True            

        return False

    ## registering a new account.
    def signup(self, first_name, sur_name, username, password, email= None):
        if (first_name and sur_name and username and password):
            for user in self.users: 
                if user['username'] == username:
                    return True
                else:
                    id = len(self.users)
                    dict = {'id': id, 'first_name': first_name, 'sur_name': sur_name, 'username': username,
                        'password': password, 'email': email}
                    
                    self.users.append(dict)
        return False

    ## List out users.
    def list_users(self):
       return self.users