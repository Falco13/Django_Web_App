from django import forms
from django.forms import Textarea

from .models import Post, Comments, User
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(label='Краткая биография', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    date_of_birth = forms.DateField(label='Дата Рождения', widget=forms.DateInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'bio', 'date_of_birth')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['theme', 'content', 'photo']
        widgets = {
            'theme': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    def clean_theme(self):
        theme = self.cleaned_data['theme']
        if re.match(r'\d', theme):
            raise ValidationError('Название не должно начинаться с цифры')
        return theme


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'rows': 5})
