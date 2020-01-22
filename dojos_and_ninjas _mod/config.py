from flask import Flask, render_template, request, redirect			
from flask_sqlalchemy import SQLAlchemy			
from sqlalchemy.sql import func 
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dojos__and_ninjas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)