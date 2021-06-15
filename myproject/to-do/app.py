from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is a Todo App'

@app.route('/add')
def add():
    return 'Add a new Todo.'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql:///to_do" #enter info
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class To_do(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date = db.Column(db.DateTime, default=db.func.now())
    completed = db.Column(db.Boolean, default=False)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')