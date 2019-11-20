from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from counter.utils import get_sevendays_readnum
from blog.models import Blog
from .form import LoginForm, RegForm



def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    read_nums, dates = get_sevendays_readnum(blog_content_type)
    context = {}
    context['read_nums'] = read_nums
    context['dates'] = dates
    return render(request, "home.html", context)

def game(request):
    return render(request, "game.html")

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
    return render(request, "login.html", context) 

def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            password = reg_form.cleaned_data['password']
            email = ''
            user = User.objects.create_user(username, email,password)
            user.save()
            user = auth.authenticate(username = username, password = password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()
    context = {}
    context['reg_form'] = reg_form
    return render(request, "register.html", context) 



