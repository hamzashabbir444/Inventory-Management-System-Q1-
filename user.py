# user.py

class User:
    users = {
        'admin@email.com': {'password': 'admin@123', 'role': 'admin'},
        'user@email.com': {'password': 'user@123', 'role': 'user'}
    }

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.role = None

    def login(self):
        """Validate login credentials and set the user role if successful."""
        user = self.users.get(self.email)
        if user and user['password'] == self.password:
            self.role = user['role']
            return True
        print("Invalid credentials.")
        return False