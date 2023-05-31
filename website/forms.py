from django import forms
from website.models import Contact,NewsLetter

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        #fields=['name', 'email']
        fields ='__all__'

class NewsLetterForm(forms.ModelForm):

    class Meta:
        model=NewsLetter
        fields='__all__'