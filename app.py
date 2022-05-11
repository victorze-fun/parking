from flask import Flask, redirect, request, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home'

@app.route('/entry', methods=['POST', 'GET'])
def entry():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('entry.html')
