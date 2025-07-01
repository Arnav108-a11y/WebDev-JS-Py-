import bcrypt
import getpass
import json

class AuthSystem:
    """A Class to handle user Authentification"""

    def __init__(self, datafile='user.json'):
        
        self.datafile = datafile
        self.current_users = None
        self.users = self._load_users()
    
    def _load_users(self):

        """Loads users from the JSON file. Returns an empty dict if file not found."""

        try:
            with open(self.datafile, 'r') as f:
               
                data = json.load(f)     
                return {user: pwd.encode('utf-8') for user, pwd in data.items()}  #String to bytes for bcrypt
        except FileNotFoundError:   # If data doesnt matches
            return {}

    def _save_users(self):
        """Saves the current user data to the JSON file."""
        with open(self.datafile, 'w') as f:
            
            data_to_save = {user: pwd.decode('utf-8') for user, pwd in self.users.items()}   #bytes to string for JSON
            json.dump(data_to_save, f, indent=4)  #python oriented data to JSON file info {.dump}

    def _hash_password(self, password):
        """Hashes a password with a random generation."""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())   #Secured password using bcrypt.gensalt instead of sta256

    def _verify_password(self, password, hashed_password):
        """Verifies a password against a stored hash."""
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)   #Cross-check using _verify_password

    def signup(self):
        """Handles the user signup process."""
        print("\n--- Create a New Account ---")
        username = input("Enter a new username: ").lower()

        if username in self.users:
            print("Username already exists. Please try another one.")    #checks from self.users, that are already registered
            return

        
        password = getpass.getpass("Enter a password: ")              #get.pass to hide entered password
        confirm_password = getpass.getpass("Confirm your password: ")

        if password != confirm_password:
            print("Passwords do not match. Please try again.")       #logic to ensure password confirmation
            return

        hashed_password = self._hash_password(password)
        self.users[username] = hashed_password
        self._save_users()                                          #User detail saved self._save_users
        print(f"Account for '{username}' created successfully!")

    def login(self):
        """Handles the user login process."""
        if self.current_user:
            print(f"You are already logged in as '{self.current_user}'.")    #If already logged in
            return

        print("\n--- Login to Your Account ---")
        username = input("Enter your username: ").lower()            #Login after initial sign up

        if username not in self.users:
            print("Username not found. Please sign up or try again.")     #If username not in self.users
            return

        password = getpass.getpass("Enter your password: ")

        if self._verify_password(password, self.users[username]):           #password verification at self.users[username]
            self.current_user = username
            print(f"Welcome back, {self.current_user}!")
        else:
            print("Invalid password. Please try again.")

    def logout(self):
        """Logs out the current user."""
        if self.current_user is None:
            print("You are not logged in.")                      #log out logic if user not logged in current_user = None
        else:
            print(f"Logging out {self.current_user}...")       
            self.current_user = None                            #After succesfull logout current_user= none
            print("You have been successfully logged out.")

    def access_protected_resource(self):
        """A sample function that requires a user to be logged in."""
        print("\n--- Protected Area ---")
        if self.current_user:
            print(f"Hello, {self.current_user}! You have access to the secret data.")
            print(" I have no idea what to write here..!")          #Resource after logging in only
        else:
            print("Access Denied. Please log in to access this resource.")
