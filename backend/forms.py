from django import forms
from frontend.models import Category, Post
from django.contrib.auth.models import User
from django.core import validators

from django.contrib.auth.forms import UserCreationForm


class Register(UserCreationForm):
    username = forms.CharField())
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField()
    password2= forms.CharField()
    class meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            return user

class CategoryForm(forms.ModelForm):
    cat_name = forms.CharField(label="Category Name", 
               widget=forms.TextInput(
               attrs={'class':'form-control', 'placeholder':'Enter Category'}))
    cat_desc = forms.CharField(label='Description', required=False,
              widget=forms.Textarea(
             attrs={'class':'form-control'}
              ))
    catch_bot = forms.CharField(required=False, 
                widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    # clean_<fieldname> is use to validate for just one field
    def clean_cat_name(self):
        cat = self.cleaned_data.get('cat_name')
        if Category.objects.filter(cat_name=cat).exists():
            raise forms.ValidationError(f'{cat} already exist')
        return cat

    class Meta():
        fields = '__all__'
        model = Category
