from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)
user={"jagan":"123456"}

@app.route('/',methods={"GET","POST"})
@app.route('/login',methods={"GET","POST"})
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] not in user or request.form['password'] != user[request.form['username']]:
            error="Invalid Credentials"
        else:
            details="Hello! "+request.form['username']
            return render_template("Success.html",details=details)
    return render_template('login.html', error=error)

@app.route('/register',methods={"GET","POST"})
def register():
    error = None
    if request.method == 'POST':
        user[request.form['username']]=request.form['password']
        return render_template('rsuccess.html')
    return render_template('register.html', error=error)


if __name__=="__main__":
    app.run(debug=True)