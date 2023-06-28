<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, render_template
>>>>>>> b2d099fb31dbbdf45a743b2361862163576a81ed


app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
app.config.from_pyfile("config.py")

<<<<<<< HEAD
@app.route('/')
def index():
    return "<h1>Hello World !</h1>"

# app.add_url_rule("/","index",index)

@app.route("/user/<name>")
def user(name: str):
    return "<h1>Hello , {}!</h1>".format(name)

# @app.route("/user1/<name>")
# def user1(name):
#     return "<h1>Bye, {}!</h1>".format(name)

if __name__ == "__main__":
=======

# @app.route('/')
# def home():
#     return render_template("home.html")

# @app.route("/user/<name>")
# def index(name):
#     return render_template("home.html", name=name)

# @app.route("/user/<name>/<int:index>")
# def index(name, index):
#     mylist = ['elemento1', 'elemento2', 'elemento3', 'elemento4']
#     mydict = {'key': 'valor'}
#     mytuple = ('tuple1', 'tuple2', 'tuple3', 'tuple4')
#     return render_template("test.html", name=name, myindex=index, mylist=mylist, mydict=mydict, mytuple=mytuple)


# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0",port=5000)

@app.route('/')
def index():
    return "<h1>Hello World!!</h1>"

@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)

if __name__ == '__main__':
>>>>>>> b2d099fb31dbbdf45a743b2361862163576a81ed
    app.run(debug=True)