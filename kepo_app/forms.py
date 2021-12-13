from django import forms
from kepo_app.models import Category, Article
from django.core.exceptions import ValidationError

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=Category._meta.get_field("name").max_length, help_text="Enter the category name!",)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Category
        fields = ('name',)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=Article._meta.get_field("title").max_length, help_text="Title",
    )
    content = forms.CharField(widget=forms.Textarea, help_text="Content",)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Article
        exclude = ('category',)