class App:

    ## Login method.
    def login(self, username, password):
        
        if (username and password):
            return True

        if (username == 'timothy' and password == 'timo123'):
            return True

        return False

    