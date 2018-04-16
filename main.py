from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!doctype html>
<html>
    <head>
        <style>
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>Signup</h1>
        <form action="/welcome" method="post">
            <label>Username:
                <input id="user_name" name="user_name" type="text"/>
            </label>
            <label>Password 
                <input name="password" type="password"/>
            </label>
            <label>Verify Password
                <input name="password_ver" type="password"/>
            </label>
            <label>Email (optional):
                <input name="email" type="text" />
            </label>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/welcome", methods=['POST'])
def welcome():
    user_name= request.form['user_name']
    return '<h1>Hello, ' + user_name + '</h1>'

app.run()