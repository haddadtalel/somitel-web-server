from webserver import app , db
from flask import *

@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template('home.html')