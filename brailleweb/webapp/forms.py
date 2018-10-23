from django import forms
from .models import UploadFile, Text


class UploadFileForm(forms.ModelForm):
    
    class Meta:
        model = UploadFile
        exclude = []

class DefaultForm(forms.ModelForm):
    
    class Meta:
        model = Text
        exclude = []