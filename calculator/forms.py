from django import forms

class Inventory(forms.Form):
    paste_inventory = forms.CharField(label="Paste Inventory", max_length=900000)