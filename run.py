from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def home():

    return render_template('index.html')

if __name__ == '__main__':
    # 코드를 수정하면 실시간 리로드되어 반영됨
    app.run(debug=True)