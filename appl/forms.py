from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from appl.models import User


class UserForm(FlaskForm):
    """
        Form for User Registration
    """
    name = StringField('Name', validators=[
                       DataRequired(), Length(min=6, max=28)])
    username = StringField('Username', validators=[
        DataRequired(), Length(min=4, max=28)])
    email = StringField('Email', validators=[
        DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        """
            If email is entered that is already
            existing in DB then error is raised.
        Args:
            email (String): email entered in form.

        Raises:
            ValidationError: Choose different mail
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Choose differnet email')

    def validate_username(self, username):
        """
            If username is entered that is already
            existing in DB then error is raised.
        Args:
            username (String): username entered in form.

        Raises:
            ValidationError: Choose different username
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Choose differnet username')


class UserLogin(FlaskForm):
    """
        Form for User Login
    """
    email = StringField('Email', validators=[
                        DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class BlogForm(FlaskForm):
    """
        Form for Blog
    """
    title = StringField('Title', validators=[DataRequired()])
    intro = TextAreaField('Intro', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    """
        Form for Comment
    """
    comment = StringField('Comment', validators=[Length(max=100)])
    submit = SubmitField('Done')
