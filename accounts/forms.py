from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as UserForm, UsernameField
from django import forms
from django.core.exceptions import ValidationError

from accounts.models import Profile


class UserCreationForm(UserForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not first_name and not last_name:
            self.add_error('first_name', 'You must fill in at least one of the following: First name or Last name!')
        return cleaned_data


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'First name', 'last_name': 'Last name', 'email': 'Email'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'github', 'about_info']
