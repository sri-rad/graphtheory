from flask import Flask, render_template, url_for, request
from make_graph import render_graph
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/barpie')
def create_barpie():
    return render_template('barpie.html')

@app.route('/stackbar')
def create_stackbar():
    return render_template('stackbar.html')

@app.route('/graph_theory', methods = ['GET','POST'])
def hello_world():
    data = request.form
    img_name = 'graph' + str(random.randint(0, 100))+'.png'
    render_graph(data, img_name)
    return render_template('graph.html', data = {'name': img_name})

if __name__=='__main__':
    app.run()