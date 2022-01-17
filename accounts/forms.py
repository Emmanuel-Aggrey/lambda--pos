
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Group

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    position = forms.ModelChoiceField(queryset=Group.objects.all(),required=True,empty_label='Selected position')
    
    

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username','first_name','last_name','position','phone','email','business','password1','password2']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email','position','business')


