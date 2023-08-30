from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Email
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e71121f8359c7c241f56e489f91f32d7'


class PaymentForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    amount = DecimalField('Amount to Pay (in NGN)', places=2, validators=[DataRequired()])
    submit = SubmitField('Pay Now')
