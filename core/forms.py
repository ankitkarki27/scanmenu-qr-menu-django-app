from django import forms

class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(label='Restaurant Name', max_length=100)
    url = forms.URLField(label='URL', max_length=200)
    
    