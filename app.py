from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return '메인페이지'
    
@app.route('/move/<name>')
def daver(name):
    if name == "daum":
        return redirect(url_for("daum"))
    elif name == "naver":
        return redirect(url_for("naver"))
@app.route("/daum")
def daum():
    return redirect("https://www.daum.net/")
@app.route("/naver")
def naver():
    return redirect("https://www.naver.net/")
if __name__ == '__main__':
    with app.test_request_context():
        print(url_for("daum"))
    app.run(debug=True)
