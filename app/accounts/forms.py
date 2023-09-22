from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','name','phone','gender']

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['email','profile_pic','name','phone','gender']

class CustomUserChangeFormAdmin(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'