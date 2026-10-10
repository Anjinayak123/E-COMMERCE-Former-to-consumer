from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ReviewForm(FlaskForm):
    rating = SelectField('Rating', coerce=int, choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], validators=[DataRequired()])
    comment = TextAreaField('Review Comment', validators=[DataRequired(), Length(min=5)])
    submit = SubmitField('Submit Review')

class SearchForm(FlaskForm):
    search = StringField('Search')
    category = SelectField('Category', coerce=int, choices=[(0, 'All Categories')])
    submit = SubmitField('Filter')

class CartUpdateForm(FlaskForm):
    submit = SubmitField('Update Cart')

class CheckoutForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=100)])
    address_line = StringField('Address', validators=[DataRequired(), Length(min=5, max=200)])
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=50)])
    postal_code = StringField('Postal Code', validators=[DataRequired(), Length(min=4, max=20)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=7, max=15)])
    payment_type = SelectField('Payment Method', choices=[('cod', 'Cash on Delivery'), ('card', 'Debit/Credit Card'), ('upi', 'UPI')], validators=[DataRequired()])
    submit = SubmitField('Place Order')
