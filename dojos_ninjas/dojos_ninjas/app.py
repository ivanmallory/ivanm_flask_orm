from flask import Flask, render_template, redirect, request			
from flask_sqlalchemy import SQLAlchemy			
from sqlalchemy.sql import func 
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dojos_ninjas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Dojo(db.Model):
    __tablename__ = "dojos"		
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    city = db.Column(db.String(45))
    state = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())    
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Ninja(db.Model):
    __tablename__ = "ninjas"	
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    dojos_id = db.Column(db.Integer, db.ForeignKey("dojos.id"))
    dojo = db.relationship("Dojo", foreign_keys=[dojos_id], backref="ninjas", cascade="all")
    created_at = db.Column(db.DateTime, server_default=func.now())    
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def full_name(self):
        return self.first_name + '' + self.last_name

@app.route('/')
def index():
    all_dojos = Dojo.query.all()
    return render_template("index.html", all_dojos = all_dojos)

@app.route('/add_dojo', methods=["POST"])
def add_dojo():
    new_dojo = Dojo(name=request.form['name'], city=request.form['city'], state=request.form['state'])
    db.session.add(new_dojo)
    db.session.commit()
    
    return redirect('/')

@app.route('/add_ninja', methods=["POST"])
def add_ninja():
    new_ninja = Ninja(first_name=request.form['first_name'], last_name=request.form['last_name'], dojos_id=request.form['dojo'])
    db.session.add(new_ninja)
    db.session.commit()
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)