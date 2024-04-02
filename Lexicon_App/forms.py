from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class admin_reg_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

