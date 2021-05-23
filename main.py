from flask import Flask, flash, request, render_template, url_for, session, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
app.secret_key = "user_credentials"

mysql = MySQL()
# MYSQL cofigurations
app.config['MYSQL_DATABASE_USER'] = 'zeusgod'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hgt.22-3'
app.config['MYSQL_DATABASE_DB'] = 'scrap_user'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('mainactivity.html',username=username)
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_credentials = {'patrick': 'pass123', 'james': 'pass456'}
    user_cred = list(login_credentials.keys())
    pass_cred = list(login_credentials.values())
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in user_cred and password in pass_cred:
            session['username'] = username
            flash('You were Successfully Logged in')
            return redirect(url_for('index'))
        else:
            flash("Invalid Login Credentials")

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
