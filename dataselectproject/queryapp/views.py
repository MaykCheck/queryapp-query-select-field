from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from .forms import UserRegistrationForm, LoginForm, DevletForm, DevletEditForm
from .models import Devlet, Şehirler

# Create your views here.

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['Şifre'])
            user.save()
            return redirect('http://127.0.0.1:8000/login/')
    else:
        user_form = UserRegistrationForm()
    return render(request,'queryapp/register.html', {
        'user_form':user_form,
        })

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['KullanıcıAdı'],
                password=data['Şifre']
            )
            if user is not None:
                login(request, user)
                #toplantılar = Toplantı.objects.all() direkt anasayfaya yönlendirebilmek için burayı kaldırdık
                return redirect('http://127.0.0.1:8000/')
            else:
                return HttpResponse("Kullanıcı Adı veya Şifre Hatalı!")
    else:
        form = LoginForm()
    return render(request,'queryapp/login.html',{
        'form':form
    })


def index(request):
    devletler = Devlet.objects.all()
    return render(request, 'queryapp/index.html',{
        'devletler':devletler
    })

def devlet_ekle(request):
    if request.method == 'POST':
        form = DevletForm(data=request.POST)
        if form.is_valid():
            yeni_devlet = form.save(commit=False)
            yeni_devlet.user = request.user
            yeni_devlet.save()
            form.save_m2m()
            return redirect('http://127.0.0.1:8000/')
        else:
            print(form.errors)
    else:
        form = DevletForm(data=request.GET)
    return render(request, 'queryapp/devlet_ekle.html',{
        'form':form
    })

def details(request, slug):
    devlet = get_object_or_404(Devlet, slug=slug)
    if request.method == 'POST':
        form = DevletEditForm(instance=devlet, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
        else:
            print(form.errors)
    else:
        form = DevletEditForm(instance=devlet)
    return render(request, 'queryapp/details.html', {
        'devlet':devlet,
        'form':form
    })

def delete_devlet(request, slug):
    devlet = get_object_or_404(Devlet, slug=slug)
    if request.user == devlet.user:
        devlet.delete()
        return redirect('http://127.0.0.1:8000/')
    else:
        return HttpResponseForbidden("Bu devleti siz yıkamazsınız...")
