- 소프트웨어 개발 내에서 데이터 관리 및 조작에서 수행되는 네 가지 필수 작업을 나타냄
- 이러한 작업은 데이터베이스 또는 데이터 스토리지 시스템과 상호 작용하는 대부분의 애플리케이션의 중추를 형성

|   이름   | 조작  |
| :----: | --- |
| CREATE | 생성  |
|  READ  | 조회  |
| UPDATE | 수정  |
| DELETE | 삭제  |
# 🌐 파이썬 기반 Web Framework

| **특징**  |   **Django**   |     **Flask**     |
| :-----: | :------------: | :---------------: |
|   **유형**    | 기능이 풍부한 프레임 워크 |     가벼운 프레임워크     |
| **사용 용이성**  |     더 복잡함      |      시작하기 쉬움      |
|  **내장 도구**  |    많은 도구 포함    |     필요한 도구 추가     |
| **프로젝트 크기** |  대규모 프로젝트에 적합  | 소규모에서 중규모 프로젝트 적합 |
|  **학습 곡성**  |     더 가파름      |       더 쉬움        |

# 플라스크 (Flask)
- 파이썬 웹 프레임워크
- 마이크로 웹 프레임워크
- 확장성 있는 설계
- 플라스크에서 프로젝트는 하나의 웹 사이트
- 플라스크 프로젝트를 생성하려면 웹 사이트를 한 개 생성하는 것과 같다
- 그리고 플라스크 프로젝트 안에는 보통 한 개의 플라스크 애플리케이션이 존재

## 파이썬 가상 환경
- 파이썬 가상환경은 파이썬 프로젝트를 격리된 환경에서 실행할 수 있도록 도와주는 도구
![[화면 캡처 2025-04-21 094141.jpg]]

# ⛏️ flask 사용하기

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_flask():
    return 'Hello, Flask App2!'
```
## 코드 리뷰
- 📦 `from flask import Flask`
	- Flask라는 웹 프레임워크에서 `Flask` 클래스를 가져온다.
	- Flask는 파이썬으로 웹 서버를 쉽게 만들 수 있게 도와주는 도구
- 🚀 `app = Flask(__name__)`
	- Flask 애플리케이션 객체를 생성
	- `__name__`은 현재 모듈의 이름을 의미하며, Flask가 어디서 실행되는지를 알게 해줌
	- 객체 `app`이 웹 서버 역할을 하게 된다
- 🔗 `@app.route('/')`
	- **데코레이터**라는 문법
	- `/` 는 홈페이지 주소를 의미
	- 이 줄은 사용자가 웹 브라우저에서 이 주소로 접속했을 때 어떤 동작을 할지 연결해줌
- 💬 `def hello_flask():`
	- 위의 route로 접속하면 실행할 함수
	- 즉, 사용자가 홈페이지에 접속하면 이 함수가 실행
- 📝 `return 'Hello, Flask App2!'`
	- 웹 브라우저에 이 문자열이 보이도록 한다.
	- 결과적으로 사용자가 웹사이트에 접속하면 `Hello, Flask App2!`라는 문구가 보임

## flask 실행하기
```cmd
Flask run
```

## 버그 확인하기
```cmd
set FLASK_DEBUG=true 
```

## 배치 파일 만들기
```bash
@echo off
cd C:\Users\kanga\Desktop\MS\CRUD
set FLASK_APP = app
set FLASK_DEBUG=true
C:\Users\kanga\Desktop\MS\aa\Scripts\activate
```

# 프로젝트 구조
- models.py : 데이터베이스 처리 파일
- forms.py : 서버로 전송된 폼 처리 파일
- views 디렉토리 : 화면 구성
- static 디렉토리 : CSS, 자바스크립트, 이미지 파일 등 저장
- templates 디렉토리 : HTML 파일 저장
- config.py : app 프로젝트 설정 파일

```bash
/myproject                  ← 전체 프로젝트 폴더
│
├── config.py              ← 설정 파일 (환경변수, DB URI 등)
│
└── /app                   ← 실제 앱 코드가 들어있는 폴더
    │
    ├── __init__.py        ← 앱을 생성하고 설정을 적용하는 초기화 파일
    ├── models.py          ← 데이터베이스 모델 정의
    ├── forms.py           ← 폼 처리 클래스들 정의 (Flask-WTF 등)
    │
    ├── /views             ← 라우팅 처리 (Blueprint 기반 분리 가능)
    │   └── (예: home.py, auth.py 등)
    │
    ├── /templates         ← HTML 템플릿 파일들
    │   └── layout.html, index.html 등
    │
    └── /static            ← 정적 파일 (CSS, JS, 이미지)
        └── style.css, app.js, logo.png 등
```

# 라우팅(Routing)
- Route는 명사로 한 곳에서 다른 곳으로 가기 위한 <mark style="background: #FFF3A3A6;">길, 경로</mark>
- 라우팅 : 어떤 데이터를 목적지까지 보내기 위한 <mark style="background: #FFF3A3A6;">경로를 선정하는 과정</mark>
- 라우팅 프로토콜 : 라우팅을 할 때 어떻게 데이터가 목적지까지 도달할 길을 만들지를 정의한 <mark style="background: #FFF3A3A6;">규칙, 규약</mark>

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
@app.route('/index/')
def index():
    return 'Hello index page'

@app.route('/about/')
def about():
    return '회사소개'

@app.route('/contect/')
def contect():
    return '여기로 연락하세요'

@app.route('/login/')
def login():
    return '아이디와 비밀번호를 입력하세요'
```

```bash
Flask routes
```

```plain text
Endpoint  Methods  Rule
--------  -------  -----------------------
about     GET      /about/
contect   GET      /contect/
index     GET      /
login     GET      /login/
static    GET      /static/<path:filename>
```

# 블루프린트 (Blueprint)
- 라우팅 함수
- URL과 함수의 <mark style="background: #BBFABBA6;">매핑을 관리</mark>하기 위해 사용하는 클래스

## Flask의 블루프린트
- 애플리케이션의 구조를 모듈화하고 코드를 정리하기 위해 사용하는 도구
- Flask 애플리케이션의 특정 부분을 캡슐화하여 독립적으로 관리할 수 있도록 해줌

