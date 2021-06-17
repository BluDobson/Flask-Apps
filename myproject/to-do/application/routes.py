from application import app, db
from application.models import To_do
from flask import Flask, render_template

@app.route('/')
def home():
    all_to_do = To_do.query.all()
    return render_template('list.html', to_do = all_to_do)

@app.route('/add')
def add():
    new_to_do = To_do(title="Clean room", description="Put away clothes and vacuum the floor", completed=False)
    db.session.add(new_to_do)
    db.session.commit()
    return 'Added a new Todo.'

@app.route('/complete/<tdid>')
def completed(tdid):
    to_do = To_do.query.get(tdid)
    to_do.completed = True
    db.session.commit()
    return 'To-do updated!'

@app.route('/incomplete/<tdid>')
def incomplete(tdid):
    to_do = To_do.query.get(tdid)
    to_do.completed = False
    db.session.commit()
    return 'To-do updated!'