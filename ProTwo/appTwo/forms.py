from django import forms
from appTwo.models import Site
from appTwo.models import Document


class NewSiteForm(forms.ModelForm):
    class Meta():
        model = Site
        #EXCLUDE sieid
        fields = '__all__'
        

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )


class EstimateForm(forms.ModelForm):
    class Meta():
        model = Site
        fields = '__all__'
