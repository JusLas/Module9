from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, NumberRange
from datetime import date


class BookForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    publication_year = IntegerField(
        'Rok publikacji', validators=[
            DataRequired(),
            NumberRange(1, date.today().year)])
    read = BooleanField('Czy przeczytana?')
    lent = BooleanField('Czy pożyczona?')
