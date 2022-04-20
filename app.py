from flask import *


app = Flask(__name__)


##################### HOME PAGE #########################
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

##################### REDIRECT #########################
@app.route('/')
def index():
    return redirect(url_for('index'))

##################### MAIN #########################
@app.route('/index/ ', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

##################### TEST #########################
with app.test_request_context():
    print(url_for('index'))
    print(url_for('index', _external=True))
    print(url_for('error'))
    print(url_for('error', _external=True))


if __name__ == '__main__':
    app.debug = True
    app.run() #go to http://localhost:5000/ to view the page.
