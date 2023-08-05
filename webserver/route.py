from flask import Blueprint,render_template

api = Blueprint('main', __name__)

@api.route('/')
def index():
   return render_template("home.html")

@api.route('/login', methods=['GET', 'POST'])
def login():
   return render_template('login.html')

@api.route('/signUp', methods=['GET', 'POST'])
def signUp():
   return render_template('sign_up.html')