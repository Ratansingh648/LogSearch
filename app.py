# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:47:29 2020

@author: Ratan Singh
"""

from flask import Flask, render_template, request, redirect
import os
import pandas as pd

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = "static/uploads"



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        return render_template('LogSearch.html', query = query)
    else:
        return render_template('LogSearch.html', query = "")



@app.route('/data')
def getData():
    query = request.args['query']
    print("*"*5)
    print(query)
    data = {}
    if query != "":
        data = {'cols' : ['col1', 'col2'],'rows' : [{'ColA': '1', 'ColB': 'ratan', 'ColC': 'nonpecalc'}, {'ColA': '2', 'ColB': 'Mayank', 'ColC': 'nonpecalc'}]}
    return data



if __name__ == "__main__":
    app.run(debug=True)