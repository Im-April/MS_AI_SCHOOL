from flask import Flask

app = Flask(__name__)

from .views import main_view, auth_view, board_view
app.register_blueprint(main_view.bp)
app.register_blueprint(auth_view.bp)
app.register_blueprint(board_view.bp)

# @app.route('/')
# @app.route('/home/')
# @app.route('/index/')
# def index():
#     return 'Hello index page'

# @app.route('/about/')
# def about():
#     return '회사소개'

# @app.route('/contact/')
# def contact():
#     return '여기로 연락하세요~'

# @app.route('/login/')
# def login():
#     return '아이디와 비번으로 로그인'

# @app.route('/board/')
# def board():
#     return '게시판'

# @app.route('/board/<id>')
# def board_view(id):
#     print(type(id))
#     return f'게시판 {id} 글 내용'