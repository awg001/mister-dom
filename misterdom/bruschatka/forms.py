from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Bruschatka
        fields = '__all__'

    # title = forms.CharField(max_length=255, label="Заголовок")
    # slug = forms.SlugField(max_length=255, label="URL")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Характристики")
    # price = models.DecimalField(max_digits=10, decimal_places=0)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Вид")
