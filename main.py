from flask import Flask , render_template
from forms import RegistrationForm , LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '36a0b7911be0f3f0139d8bf9f498ecf3'

posts = [
    {
        "author" : "Rokon",
        "age" : "23",
        "content" : "hello nai",
        "height" : "183"
    },
    {
        "author" : "Shammo",
        "age" : "24",
        "content" : "Biri ta de",
        "height" : "180"
    },
    {
        "author" : "Esmay",
        "age" : "23",
        "content" : "taka nai",
        "height" : "165"
    },
    {
        "author" : "Nahid",
        "age" : "22",
        "content" : "pani an ja",
        "height" : "167"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html' , posts = posts , titl = 'home')



@app.route("/about")
def about():
    return render_template('about.html' , titl = 'about')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html' , titl = 'Register' , form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html' , titl = 'login' , form = form)

if __name__ == '__main__':
    app.run(debug = True)
    