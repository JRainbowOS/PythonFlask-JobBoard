from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/jobs')
def jobs():
    global path_to_template 
    path_to_template = 'index.html'
    return render_template(path_to_template)

