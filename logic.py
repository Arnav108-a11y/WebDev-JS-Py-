from flask import Flask, render_template, request, redirect, url_for, flash, session
from Auth_system import AuthSystem

app = Flask(__name__)
app.secret_key = 'your_super_secret_key_change_me'

auth = AuthSystem()

@app.route('/')
def index():
    # If user is already logged in, redirected to dashboard
    if 'username' in session:
        return redirect(url_for('dashboard'))
    # Otherwise redirect to login page
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']

        # Use the auth system to verify credentials
        if username in auth.users and auth._verify_password(password, auth.users[username]):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))
    
    # For a GET request, just show the login page
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']
        
        if username in auth.users:
            flash('Username already exists.')
            return redirect(url_for('signup'))
        
        # Use auth system to create a new user
        hashed_password = auth._hash_password(password)
        auth.users[username] = hashed_password
        auth._save_users()
        
        flash('Account created successfully! Please log in.')
        return redirect(url_for('login'))
        
    # For a GET request, just show the signup page
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    # This is a protected route.
    # If the user is not in the session, redirect them to the login page.
    if 'username' not in session:
        flash('You must be logged in to view this page.')
        return redirect(url_for('login'))
    
    # If they are logged in, show them the dashboard
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('username', None) # Remove the user from the session
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

    ##After running this in the directory in which this .py file resides, with the command python logic.py, the terminal is now a web server
    # the users.json file will now register all the input users credentials with salt characters due to bcrypt
    ## I couldnt add this comment in .json as the damn thing doesnt support comments :)
