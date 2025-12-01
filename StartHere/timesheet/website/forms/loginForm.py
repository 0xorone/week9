from django.forms import Form, CharField, PasswordInput
# from website.models import Credentials

class LoginForm(Form):
    username = CharField(max_length=20)
    password = CharField(widget=PasswordInput())

