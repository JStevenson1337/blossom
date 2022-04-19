from flask import render_template, Flask, request, make_response
from models import Calendar, Event

app = Flask(__name__)


##################### HOME PAGE #########################
@app.route("/")
def home():
    return render_template("home.html")



if __name__ == '__main__':
    app.debug = True
    app.run() #go to http://localhost:5000/ to view the page.
