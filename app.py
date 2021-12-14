from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return '서버의 홈 화면입니다.'

@app.route('/mypage')
def mypage():
   return '마이 페이지입니다.'

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)