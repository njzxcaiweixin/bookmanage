from django import forms


class ContactForm(forms.Form):
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=100)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)
