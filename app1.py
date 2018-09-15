from flask import Flask, request, render_template
from random import randint

dynamic_url = str(randint(100000, 900000))

app = Flask(__name__)

@app.route('/' + dynamic_url)
def attendance():
    return 'Hi there'

@app.route('/qr')
def qr():
    url_root = request.url_root
    url = url_root + dynamic_url
    return render_template('qr.html', dynamic_url=url)

app.run(port=5555, debug=True)
