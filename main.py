# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Conectando SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portafolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Creación de una tabla
class Card(db.Model):
     #Creación de columnm
    #id
    id = db.Column(db.Integer, primary_key=True)
    #email
    email = db.Column(db.String(30), nullable=False)
    #Texto
    text = db.Column(db.Text, nullable=False)
@app.route('/', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        email= request.form['email']
        text = request.form['text']
        
        comen = Card(email=email, text =text )
        db.session.add(comen )
        db.session.commit()
        return redirect('/')
    else:    
        return render_template('index.html')
    
@app.route('/')
def index():
    return render_template('index.html')




# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_db = request.form.get('button_db')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    return render_template('index.html', button_python=button_python, button_db = button_db, button_discord=button_discord, button_html=button_html)


if __name__ == "__main__":
    app.run(debug=True)
