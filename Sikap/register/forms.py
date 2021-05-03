from django import forms
from login.models import *

class userForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'account_type',
            'email',
            'password',
            'name',
            'surname',
            'user_type',
            'isVerified',
            'companyName',
            'industry',
            'region',
            'province',
            'city',
            'age',
        ]