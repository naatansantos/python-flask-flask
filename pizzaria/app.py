#python -m venv venv
#.\venv\Scripts\activate
#pip install flask
# pip install python-dotenv
#pip freeze > requirements.txt
#pip install -r requirements.txt
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cardapio')
def cardapio():
    pizzas = [
        {
            "nome": "Calabresa",
            "ingredientes": "Molho de tomate, mussarela, calabresa, cebola e orégano",
            "preco": 30.00
        },
        {
            "nome": "Mussarela",
            "ingredientes": "Molho de tomate, mussarela e orégano",
            "preco": 25.00
        },
        {
            "nome": "Portuguesa",
            "ingredientes": "Molho de tomate, mussarela, presunto, ovos, cebola, azeitona e orégano",
            "preco": 35.00
        }
    ]
    return render_template("cardapio.html", pizzas=pizzas)


@app.route('/avaliacoes')
def avaliacoes():
    avaliacoes = [
        {"cliente": "João", "comentario": "Adorei os sabores!"},
        {"cliente": "Maria", "comentario": "Atendimento excelente!"},
        {"cliente": "Carlos", "comentario": "A melhor que está tendooo!"}
    ]
    return render_template("avaliacoes.html", avaliacoes=avaliacoes)


@app.route('/faleconosco', methods=['GET', 'POST'])
def faleconosco():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        mensagem = request.form.get('mensagem')
        return f"Obrigado pela mensagem, {nome}!"
    return render_template("faleconosco.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        if usuario == "admin" and senha == "1234":
            return "Login realizado com sucesso!"
        return "Usuário ou senha inválidos!"
    return render_template("login.html")

if __name__=='__main__':
    app.run()