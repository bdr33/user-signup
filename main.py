from flask import Flask, request
import cgi
import os
import jinja2

template_dir= os.path.join(os.path.dirname(__file__), 'templates')
jinja_env= jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template = jinja_env.get_template('index_form.html')
    return template.render()

@app.route("/validate-form", methods=['POST'])
def validate_form():

    user_name= request.form['user_name']
    password= request.form['password']
    password_ver= request.form['password_ver']
    email= request.form['email']

    user_name_error= ''
    password_error= ''
    password_ver_error=''
    email_error=''

    if user_name=="":
        user_name_error = 'You must enter a username'
    else: 
        if len(user_name) <3 or len(user_name) >20:
            user_name_error= 'Your username must be between 3 and 20 characters long'
        else: 
            if " " in user_name:
                user_name_error= 'Your username cannot contain any spaces'

        
    if password=="":
        password_error = 'You must enter a password'
    else: 
        if len(password) <3 or len(password)>20:
            password_error= 'Your password must be between 3 and 20 characters long'
        else: 
            if " " in password: 
                password_error= 'Your password cannot contain any spaces'
            
    if password_ver == "" or password_ver != password:
        password_ver_error = "Passwords don't match"
    
    if email !="":
        if len(email) <3 or len(email)>20 or " " in email: 
            email_error='Please enter a valid email'
        else: 
            if email.count('@') != 1 or email.count('.') !=1:
                email_error='Please enter a valid email'
        

    if not user_name_error and not password_error and not password_ver_error and not email_error:
        template = jinja_env.get_template('welcome.html')
        return template.render(user_name=user_name)

    else: 
        template = jinja_env.get_template('index_form.html')
        return template.render(user_name=user_name, password='', 
        password_ver='', email=email, user_name_error=user_name_error, password_error=password_error,
         password_ver_error=password_ver_error, email_error=email_error)


app.run()