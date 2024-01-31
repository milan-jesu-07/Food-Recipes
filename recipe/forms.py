from django.forms import ModelForm
from .models import Recipe
from django import forms


class CreateRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        widgets = {'ingredient': forms.Textarea(),'How_to_make':forms.Textarea(),
                   'created_by': forms.HiddenInput()}