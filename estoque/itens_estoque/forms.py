from django import forms
from .models import ItemEstoque

class NovoItem(forms.ModelForm):
    class Meta:
        model = ItemEstoque
        fields = '__all__'

class ItemEstoqueForm(forms.ModelForm):
    class Meta:
        model = ItemEstoque
        fields = '__all__'
