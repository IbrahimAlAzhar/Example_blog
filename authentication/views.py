from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    logout(request)
    return render(request,'authentication/logged_out.html')


def welcome(request):
    return render(request,'authentication/welcome.html')


def register(request):
    """Register a new user"""
    if request.method != 'POST':
        form = UserCreationForm() # usercreationform is django build in form
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user) # after authenticated then login
            return HttpResponseRedirect(reverse('welcome'))
    context = {'form': form}
    return render(request,'authentication/register.html',context)
