from typing import Any, Optional
from django.db import models
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import UpdateView
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
# Create your views here.



def signup (request):
    form = SignUpForm()
    if request.method == "POST":
        
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('index')
           
           

    return render(request, 'signup.html', {'form':form})


class UserUpdateView(UpdateView):
    model=User
    fields =('first_name','last_name', 'email',)
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user