from django import forms


class SumaForm(forms.Form):
    numero1 = forms.DecimalField(label="Primer número")
    numero2 = forms.DecimalField(label="Segundo número")