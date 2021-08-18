from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import ResgistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        "author":"Shubham",
        "title": "Blog post 1",
        "date_posted": "09 Aug 2021",
        "content":"first post content"
    },
    {
        "author":"Pratik",
        "title": "Blog post 2",
        "date_posted": "10 Aug 2021",
        "content":"Second post content"
    }
]

@app.route("/")
@app.route("/Home")
def Home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title = "About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = ResgistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('Home'))
    return render_template("register.html", title = "Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('Home'))
        else:
            flash('Login Unsuccessfull, Please check your username and password', 'danger')

    return render_template("login.html", title = "Login", form=form)