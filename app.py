from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import pandas as pd

app = Flask(__name__)

## Database Connection
path='/Users/Aman.Kalra/Desktop/Flask WebApp/database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+path
db=SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(1000))
    complete=db.Column(db.Boolean)

@app.route('/')
def index():
    incomplete=Todo.query.filter_by(complete=False).all()
    complete=Todo.query.filter_by(complete=True).all()
    print_table_contents()
    return render_template('index.html',complete=complete,incomplete=incomplete)

def print_table_contents():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query( "SELECT * FROM Todo", conn )
    df.to_csv('demo.csv')

@app.route('/add',methods=['POST'])
def add():
    item = Todo(text=request.form['todoitem'],complete=False)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('index')) 

@app.route('/complete/<id>')
def complete(id):
    item = Todo.query.filter_by(id = int(id)).first()
    item.complete=True
    db.session.commit()
    return redirect(url_for('index')) 

@app.route('/incomplete/<id>')
def incomplete(id):
    item = Todo.query.filter_by(id = int(id)).first()
    item.complete=False
    db.session.commit()
    return redirect(url_for('index')) 

@app.route('/delete/<id>')
def delete(id):
    item = Todo.query.filter_by(id = int(id)).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index')) 


if __name__=="__main__":
    db.create_all()
    app.run(debug=True)