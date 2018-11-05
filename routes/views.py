from app import app


@app.route('/')
def home():
    return 'Home'


@app.route('/term')
def term():
    return render_template('term.html')


@app.route('/parent')
def parent():
    return render_template('parent.html')


@app.route('/child')
def child():
    return render_template('child.html')


@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html')


@app.route('/admission')
def admission():
    return render_template('admission.html')
