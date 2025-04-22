from flask import Blueprint, render_template

bp = Blueprint('main',__name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html', title="나의 홈페이지", username='홍길동')

@bp.route('/hello')
def hello():
    return 'Hello hello page'