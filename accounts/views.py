from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
    else:
        form = UserForm()
    data={'form':form}
    return render(request, 'accounts/signup.html', data)

def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("password_change_done")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change.html', {'form':form})
