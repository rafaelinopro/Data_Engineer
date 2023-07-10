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
<<<<<<< HEAD
# En python se manejan los datos, las variables, etc, que se mostraran en la pagina HTML.
# Por otra parte, HTML tiene un codigo interno que determina el resultado final de la vista. 
=======

@app.route('/saludo')
def saludo():
    genero = 'perro'  # Esta variable puede ser definida dinámicamente
    name = 'Carla'  # Esta también puede ser definida dinámicamente
    return render_template('saludo.html', genero=genero, name=name)

@app.route('/nombres')
def nombres():
    nombres = ['Juan', 'Ana', 'Carlos', 'María']  # Esta lista puede ser obtenida de forma dinámica
    return render_template('nombres.html', nombres=nombres)
>>>>>>> b2d099fb31dbbdf45a743b2361862163576a81ed

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)