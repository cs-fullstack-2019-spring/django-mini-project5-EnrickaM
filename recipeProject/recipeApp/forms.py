from django import forms
from .models import  CreateNewUserModel,NewrecipeModel




class CreateNewUserForm(forms.ModelForm):
    class Meta:
        model = CreateNewUserModel
        fields="__all__"






class NewrecipeForm(forms.ModelForm):
    class Meta:
        model=NewrecipeModel
        fields="__all__"