"""Routes for the flask instance"""

from flask import Flask, session, redirect, url_for, request
from markupsafe import escape

from flask import current_app as app

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s. <a href="/logout">Logout</a>' % escape(session['username'])
    else:
        return redirect(url_for('login'))
    #fi
#edef

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect('/explodash')
    else:
        return '''
            <h1> Welcome to ExploDash</h1>
            <h2> You need to Log in</h2>
            If you do not have login details, contact thies.gehrmann@uantwerpen.be
            <form method="post">
                <p><input type=text name=username>
                <p><input type=password name=password>
                <p><input type=submit value=Login>
            </form>
        '''
    #fi
#edef

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))