from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UsernameField,UserCreationForm
from django.contrib.auth.models import User
from app.models import *

# Login Form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control '}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username','password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'})}

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text','review_rating']

class DemandserviceReviewForm(forms.ModelForm):
    class Meta:
        model = DemandServiceReview
        fields = ['review_text','review_rating']

class HealthpackageReviewForm(forms.ModelForm):
    class Meta:
        model = HealthPackageReview
        fields = ['review_text','review_rating']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = HealthPackageReview
        fields = '__all__'

class DoctorReviewForm(forms.ModelForm):
    class Meta:
        model = DoctorReview
        fields = ['review_text','review_rating']

class NurseReviewForm(forms.ModelForm):
    class Meta:
        model = NurseReview
        fields = ['review_text','review_rating']


class NurseAddForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    name = forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class': 'form-control'}))

    introduction = forms.CharField(label='Introduction', widget=forms.TextInput(attrs={'class': 'form-control'}))
    p_developement = forms.CharField(label='Professional Developement', widget=forms.TextInput(attrs={'class': 'form-control'}))
    education = forms.CharField(label='Education', widget=forms.TextInput(attrs={'class': 'form-control'}))
    language = forms.CharField(label='Language', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Nurse
        fields = ['username','password','name','image','speciality','introduction','p_developement','education','experience','language','service_area','working_time']

class NurseInfo(forms.ModelForm):
    name = forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.CharField(label='Price', widget=forms.TextInput(attrs={'class': 'form-control'}))
    introduction = forms.CharField(label='Introduction', widget=forms.TextInput(attrs={'class': 'form-control'}))
    p_developement = forms.CharField(label='Professional Developement', widget=forms.TextInput(attrs={'class': 'form-control'}))
    education = forms.CharField(label='Education', widget=forms.TextInput(attrs={'class': 'form-control'}))
    language = forms.CharField(label='Language', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Nurse
        fields = ['name','image','speciality','price','introduction','p_developement','education','experience','language','service_area','working_time','is_active']

class NurseHireForm(forms.ModelForm):

    working_time = forms.CharField(label='Professional Developement', widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = NurseHire
        fields = ['service_name','service_area','working_time']


class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['first_name','last_name','email']