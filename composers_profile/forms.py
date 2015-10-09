from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import ComposersProfile,ForgotPasswordUsers


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

    def clean_username(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username', "")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("These are the wrong credentials.")
        return username


class ComposerForm(ModelForm):
    class Meta:
        model = ComposersProfile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ComposerForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['gender'].widget.attrs.update()
        self.fields['address'].widget.attrs.update({'class' : 'form-control'})
        self.fields['latitude'].widget.attrs.update({'class' : 'form-control'})
        self.fields['longitude'].widget.attrs.update({'class' : 'form-control'})
        self.fields['current_song'].widget.attrs.update({'class' : 'form-control'})
        self.fields['hit_songs'].widget.attrs.update({'class' : 'form-control'})
        self.fields['education'].widget.attrs.update({'class' : 'form-control'})
        self.fields['summary'].widget.attrs.update({'class' : 'form-control'})


class ForgotPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))

    def clean_username(self):
        cleaned_data = super(ForgotPasswordForm, self).clean()
        username = cleaned_data.get('username', "")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("You are not a authorized user.")
        return username


class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    def clean(self):
        cleaned_data = super(ResetPasswordForm, self).clean()
        password = cleaned_data.get('password', "")
        confirm_password = cleaned_data.get('confirm_password', "")
        if password != "" and password != confirm_password:
            raise forms.ValidationError("Password does not match.")
        return cleaned_data
