from flask import Blueprint,render_templatee

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_templatee("home.html")