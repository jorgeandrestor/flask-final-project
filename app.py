# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from datetime import datetime
from flask import request, redirect
from model import process_results, bender_selection, most_frequent, img_selection



# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time=datetime.now())


@app.route('/results', methods=['GET','POST'])
def results():
    if request.method == 'POST':
        # user_name=dict(request.form)
        # print(dict(request.form))
        props= most_frequent(dict(request.form))
        select=bender_selection(props)
        print(props,select)
        link= img_selection(props)
        return render_template("results.html",props=props,select=select, link=link)
    else:
        return "error"
