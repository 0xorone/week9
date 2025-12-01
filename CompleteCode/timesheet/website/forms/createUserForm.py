from django.forms import Form, CharField, PasswordInput

class CreateUserForm(Form):
    username = CharField(max_length=30)
    email = CharField(max_length=50)
    password = CharField(widget=PasswordInput())