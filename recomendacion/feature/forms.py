from django import forms
from django.core.validators import FileExtensionValidator

class UploadFileForm(forms.Form): 
    #title = forms.CharField(max_length=50)
    document = forms.FileField(validators=[FileExtensionValidator(['npy'])])
    IDs = forms.FileField()
    CSV = forms.FileField()
