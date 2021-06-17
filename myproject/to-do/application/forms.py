from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError

class entryForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired(), Length=(max=20)])
    description = StringField('Description:', validators=[Length=(max=200)])
    completed = BooleanField()