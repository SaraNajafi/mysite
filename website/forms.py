from django import forms
from website.models import Contact, NewsLetter


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)


class ContactForm(forms.ModelForm):
    # subject=forms.CharField(help_text="Do you have any questions?", widget=forms.Textarea, required=False)
    class Meta:
        model = Contact
        # fields=['name', 'email','message']
        fields = '__all__'


class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = '__all__'
