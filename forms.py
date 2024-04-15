from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log Me In!")


class AddForm(FlaskForm):
    name = StringField("Name of the game", validators=[DataRequired()])
    img_url = StringField("URL of the image", validators=[DataRequired(), URL()])
    price = StringField("Price", validators=[DataRequired()])
    submit = SubmitField("Submit")
