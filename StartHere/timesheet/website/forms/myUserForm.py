from django.forms import ModelForm, TextInput, HiddenInput
from website.models import UserDetails 

class MyUserForm(ModelForm):
    class Meta:
        model = UserDetails 
        fields = '__all__'
        widgets = {
            'userId': HiddenInput(),
            'hourlyRate': HiddenInput(),
            'phone': TextInput(),
            'routingNumber': TextInput(),
            'accountNumber': TextInput(),
        }
