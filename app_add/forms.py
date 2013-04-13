from django import forms

class Output(forms.Form):
    input1 = forms.IntegerField(max_value=1000000)
    input2 = forms.IntegerField(max_value=1000000)
