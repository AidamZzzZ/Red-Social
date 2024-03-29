from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView

class ProfileListView(ListView):
    model = Profile
    context_object_name = "profiles"
    template_name = "app/profile_list.html"

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "app/profile_detail.html"

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['bio',]
    success_url = "/"
    template_name = "app/profile_update.html"

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "app/profile_principal.html"

@login_required
def follow(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        user = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == "follow":
            user.follows.add(profile)
        elif action == "unfollow":
           user.follows.remove(profile)
        user.save()
    return render(request, "app/profile_detail.html", {'profile':profile})
                



def index(request):
    return render(request, 'app/index.html')

def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'auth/register.html', {'form':form})

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            return redirect("login")
        else:
            return render( request, 'auth/register.html', {'form':form})
        
def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('home')
        
        form = LoginForm()
        return render(request, 'auth/login.html', {'form':form})
    
    
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()} Welcome!.')
                return redirect("home")
        messages.error(request, f'Invalid username or password')
        return render(request, 'auth/login.html', {'form':form})

def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logget out')
    return redirect('login')




