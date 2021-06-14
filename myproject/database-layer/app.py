from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@35.230.141.149/example"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')