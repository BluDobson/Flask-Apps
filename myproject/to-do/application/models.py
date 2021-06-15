from application import db

class To_do(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date = db.Column(db.DateTime, default=db.func.now())
    completed = db.Column(db.Boolean)