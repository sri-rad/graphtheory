from flask import Flask, render_template, url_for, request
from make_graph import render_graph
import time

app = Flask(__name__)

@app.route('/create')
def create_page():
    return render_template('create.html')

@app.route('/graph_theory', methods = ['GET','POST'])
def hello_world():
    data = request.form
    img_name = 'graph' + str(time.time())+'.png'
    render_graph(data, img_name)
    return render_template('graph.html', data = {'name': img_name})

if __name__=='__main__':
    app.run()