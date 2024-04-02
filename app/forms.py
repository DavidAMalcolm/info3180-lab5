# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import FileField, StringField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length


class MovieForm(FlaskForm):
    title = StringField(
        "Movie Title", validators=[InputRequired(), Length(min=1, max=100)]
    )
    description = TextAreaField(
        "Description", validators=[InputRequired(), Length(min=10, max=500)]
    )
    poster = FileField(
        "Movie Poster",
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "jpeg", "png"], "Only images"),
        ],
    )
