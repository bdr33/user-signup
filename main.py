from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!doctype html>
<html>
    <head>
        <style>
            .error {{ color: red; }}
        </style>
    </head>
    <body>
        <h1>Signup</h1>
        <form action="/validate-form" method="post">
            <label>Username:
                <input id="user_name" name="user_name" type="text" value='{user_name}'/>
            </label>
            <p class="error">{user_name_error}</p>

            <label>Password 
                <input id="password" name="password" type="password" value='{password}'/>
            </label>
            <p class="error">{password_error}</p>

            <label>Verify Password
                <input id="password_ver" name="password_ver" type="password" value='{password_ver}'/>
            </label>
            <p class="error">{password_ver_error}</p>

            <label>Email (optional):
                <input id="email" name="email" type="text" value='{email}'/>
            </label>
            <p class="error">{email_error}</p>

            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(user_name='', user_name_error='', 
    password='', password_error='', password_ver='', password_ver_error='', email='', email_error='')

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
    empty_error=''

    if user_name=="":
        user_name_error = 'You must enter a username'
        
    if password=="":
        password_error = 'You must enter a password'
            
    if password_ver == "":
        password_ver_error = "Passwords don't match"
        ****return formatted form
    else:
        return '<h1>Hello, ' + user_name + '</h1>'

app.run()