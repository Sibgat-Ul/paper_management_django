from django.forms import ModelForm, Form, IntegerField, Textarea, CharField
from .models import Thesis, ThesisDescription


class ThesisForm(Form):
    title = CharField(max_length=200)
    supervisor = CharField(max_length=200)
    category = CharField(max_length=300)
    description = CharField(widget=Textarea)



