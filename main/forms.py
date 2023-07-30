from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ResponseForm(forms.Form):
    fname = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={
        "placeholder": "First name",
        "required": True,
        "rows": 2,
        "class": "form-textarea",
        }),
        label='',
        min_length=1, 
        max_length=25,
    )
    lname = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={
        "placeholder": "Last name",
        "required": True,
        "rows": 2,
        "class": "form-textarea",
        }),
        label='',
        min_length=1, 
        max_length=25
    )
    email = forms.EmailField(required=False, widget=forms.widgets.Textarea(attrs={
        "placeholder": "Email",
        "required": True,
        "rows": 2,
        "class": "form-textarea",
        }),
        label='',
        min_length=3, 
        max_length=25
    )
    response = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={
        "placeholder": "Message",
        "required": True,
        "rows": 2,
        "class": "form-textarea",
        }),
        label='',
        min_length=1, 
        max_length=100
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, label='',)
