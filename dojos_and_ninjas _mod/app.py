from flask import render_template, request, redirect
from config import app, db, func
from models import Dojo, Ninja
import routes
if __name__ == "__main__":
    app.run(debug=True)