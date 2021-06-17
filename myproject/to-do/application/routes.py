from application import app, db
from application.models import To_do
from application.forms import entryForm
from flask import Flask, render_template, request

@app.route('/')
def home():
    all_to_do = To_do.query.all()
    return render_template('list.html', to_do = all_to_do)

@app.route('/add', methods=['GET', 'POST'])
def add():
    error = ""
    form = entryForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data 
            description = form.description.data
            completed = form.completed.data
            new_to_do = To_do(title=title, description=description, completed=completed)
            db.session.add(new_to_do)
            db.session.commit()
            return f'Added a new To-do.'
        else:
            return render_template('entry.html', form=form, title="", description="")
    else:
        return render_template('entry.html', form=form)

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