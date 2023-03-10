from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)

@app.route('/',methods={"GET","POST"})
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'jagan' or request.form['password'] != '123456':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template("Success.html")
    return render_template('index.html', error=error)


if __name__=="__main__":
    app.run(debug=True)