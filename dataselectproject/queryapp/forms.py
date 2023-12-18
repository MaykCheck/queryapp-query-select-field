from django import forms
from django.contrib.auth.models import User
from .models import Devlet, Şehirler

class UserRegistrationForm(forms.ModelForm):
    Şifre = forms.CharField(label='Şifre', widget=forms.PasswordInput)
    Şifre2 = forms.CharField(label='Şifreyi Doğrula', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email')
        help_texts = {
            'username':None,
        }

class LoginForm(forms.Form):
    KullanıcıAdı = forms.CharField()
    Şifre = forms.CharField(widget=forms.PasswordInput)

demo_seçimler = (
    ("Konstantiniyye", "Konstantiniyye"),
    ("Beç", "Beç"),
    ("Venedig", "Venedig"),
    ("Napule", "Napule",),
    ("Haleb", "Haleb"),
    ("Otranto", "Otranto"),
    ("Marsilya", "Marsilya"),
    ("Rodos", "Rodos"),
    ("Gümülcine", "Gümülcine"),
    ("Graz", "Graz"),
    ("Inttal", "Inttal"),
    ("Budin", "Budin"),
)

class DevletForm(forms.ModelForm):
    şehir = forms.ModelMultipleChoiceField(queryset=Şehirler.objects.all(), required=True)
    class Meta:
        model = Devlet
        fields = ('ülke','başkent','şehir')
        widgets = {
            'ülke':forms.TextInput(attrs={"placeholder":"Ülke", "required":"True", "style":"width:40%;"}),
            'başkent':forms.TextInput(attrs={"placeholder":"Başkent", "required":"True", "style":"width:40%;"}),
            'şehir':forms.CheckboxSelectMultiple(attrs={"placeholder":"şehir seç"})
        }
        labels = {
            'ülke':'ülke',
            'başkent':'başkent',
            'şehir':'şehir',
        }

class DevletEditForm(forms.ModelForm):
    şehir = forms.ModelMultipleChoiceField(queryset=Şehirler.objects.all(), required=True)
    class Meta:
        model = Devlet
        fields = ('ülke','başkent','şehir')
        widgets = {
            'ülke':forms.TextInput(attrs={"placeholder":"Ülke", "required":"True", "style":"width:40%;"}),
            'başkent':forms.TextInput(attrs={"placeholder":"Başkent", "required":"True", "style":"width:40%;"}),
            'şehir':forms.CheckboxSelectMultiple(attrs={"placeholder":"şehir seç"})
        }
        labels = {
            'ülke':'ülke',
            'başkent':'başkent',
            'şehir':'şehir',
        }