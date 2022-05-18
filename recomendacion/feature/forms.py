from django import forms

class DocumentForm(forms.Form): 
    docfile = forms.FileField( 
        label='Select a file">file', 
        help_text='max. 42 megabytes' )
