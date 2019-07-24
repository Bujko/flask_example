from flask import Flask, request,render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/extra')
def extra():

    return render_template('extra.html', variable="Flask")

@app.route('/bare')
def bare():

    return "Hello Flask"

@app.route('getandpost',methods = ['GET', 'POST'])
def validate_app():

    if request.method == "POST":

        message = request.args['message']

        return "The message is : " + message

app.run(port=5000, debug = True)
