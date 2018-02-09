from django import forms
from django.contrib.auth.models import User
from appTwo.models import Site, Document, UserProfileInfo


class NewSiteForm(forms.ModelForm):
    class Meta():
        model = Site
        #EXCLUDE siteid
        fields = '__all__'


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )


class EstimateForm(forms.ModelForm):
    class Meta():
        model = Site
        fields = '__all__'



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    department = forms.CharField(max_length=128, required = False)
    class Meta():
        model = UserProfileInfo
        fields = ('department',)
