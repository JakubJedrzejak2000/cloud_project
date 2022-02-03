from django import forms

class YourName(forms.Form):
    your_name = forms.CharField(label = "Your Name", max_length=100, required=False)