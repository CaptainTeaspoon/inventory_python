from django import forms
from .models import Items, Usergroups, Users, Warehouse

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'barcode', 'cost', 'expiration_date', 'warehouse']

class UsergroupForm(forms.ModelForm):
    class Meta:
        model = Usergroups
        fields = ['name']

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'email', 'password', 'usergroup']
        widgets = {'password': forms.PasswordInput} # Für Passwortfelder

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name', 'usergroup']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
