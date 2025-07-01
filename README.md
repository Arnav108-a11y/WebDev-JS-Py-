I opted for the 2nd option given in the application process i.e. the Authentication system where I had to build a simple login/signup interaction with authenticating features like hashing, maintainence of user secrets and Login states, between the user and the system.
My work comprises of the usage of languages like HTML & Python, where the user input is stored as a .json type input.

1. I created 3 Web templates in HTML acting as the main portal for user view, namely Login.HTML, Signup.HTML and Dashboard.HTML. I also used Jinga2* template on my Login and Signup interfaces to show any highlated errors while rendering the logic using Flask.

2. I created the main Python file with a user.json datafile, named Auth_system.py, where I used Python classes to create a interface which deals with the user data, where to enter, how to utilise and where to store.
   I used methods like
   {_load_users,_save_users,_hash_password,_verify_password,signup, login & logout and also a access_protected_resource} with the def using AuthSystem Python class.
   I also imported modules like:
   
   bcrypt: For hashing passwords securely, using utf-8 for strings input to bytes & using bcyrpt.gensalt to generate a random salts*.
   getpass: for securely taking user input password, without showing on terminal.
   json: Storing user data in json format file type, Using datafile="user.json".

   [PS: I had to research about these modules before using them on my project, as I was figuring out which modules I might need for this project.] 

3.Further I created a Logic.py* while deals with what happens with the user interaction after the data is taken, whether to redirect, or to flag an error, or to direct either to the signup or dashboard.html interface.I used:
  Flask: A minimal web framework used to handle HTTP requests and HTML templates, defining URL routes.
  Render_template*: connects an app.route to an HTML template, seperating python logic from HTML template.
  Request: I used request.form to extract the data from my HTML template files into the logic frame, also method like GET &  
  POST from request.method. Generally used to handle Client server requests.
                 {GET: retrieve data from server, POST: send data to server}
  redirect: used to return an HTTP redirect response to to some other URL. eg. after logging out redirect to login page. 
  url_for*: Dynamic URL builer for routes based on functions. 
  [I tried using href initially which made me realise I have to update the app.route each time I use it, faced a error first    time around]
  flash: To show one time messages to user before re-direction. 
  session: Used for Individual user sessions, storing their data exclusively using cookies.

At last I had to enter a command like python logic.py using the correct dictionary path, which converted my terminal into a server with timestamps of every second. Outputs like 302, 200,404 and 500 each time a user handles it.

Each time around the data is stored in a user.json file type on VScode, showing user credentials with hashing.
