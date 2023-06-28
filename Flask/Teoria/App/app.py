from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# @app.route("/about")
# def learn():
#     return "Flask for web developers!"

@app.route("/<your_name>")
def greetings(your_name):
    """Función de vista para saludar al usuario por su nombre."""
    return "¡Bienvenido " + your_name + "!"


@app.route("/user/<name>")
def index(name):
    return render_template("home.html", name=name)

@app.route("/user/<name>/<int:index>")
def index2(name, index):
    mylist = ['elemento1', 'elemento2', 'elemento3', 'elemento4']
    mydict = {'key': 'valor'}
    mytuple = ('tuple1', 'tuple2', 'tuple3', 'tuple4')
    return render_template("test.html", name=name, myindex=index, mylist=mylist, mydict=mydict, mytuple=mytuple)
# En python se manejan los datos, las variables, etc, que se mostraran en la pagina HTML.
# Por otra parte, HTML tiene un codigo interno que determina el resultado final de la vista. 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)