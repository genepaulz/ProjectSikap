from django import forms
from posts.models import *

class postsForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = [
            'yearsOfExperience',
            'industry',
            'region',
            'province',
            'city',
            'age',
            'dateadded',
            'email',
            'isAgeViewable'
        ]