# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_birthmonth


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods=["GET", "POST"])
def results():
    print(request.form["birthmonth"])
    user_birth = request.form["birthmonth"]
    birth_stone = get_birthmonth(user_birth)
    return render_template("results.html", user_birth=user_birth, birth_stone=birth_stone)
    
