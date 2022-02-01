from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_host:
                login(request, user)
                return redirect('hostpage')
            elif user is not None and user.is_guest:
                login(request, user)
                return redirect('guest')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "logout.html", {})


@login_required()
def host(request):
    return render(request,'host.html')

@login_required()
def guest(request):
    return render(request,'guest.html')

@login_required()
def profile(request):
    return render(request, 'profile.html')