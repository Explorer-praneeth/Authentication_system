from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'messages': 'Username already exists.'})
        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, first_name=first_name, password=password)
            user.save()
            return render(request, 'login.html', {'messages': 'Registration successful. Please log in.'})
        else:
            return render(request, 'register.html', {'messages': 'Passwords do not match.'})
    return render(request,'register.html')
def login_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user  = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'home.html',{'messages':'Login successful.', 'user': user.first_name})
    return render(request,'login.html')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'user': request.user.first_name})
    return render(request, 'login.html', {'messages': 'Please log in to access the home page.'})

def logout_view(request):
    logout(request)
    return render(request, 'login.html', {'messages': 'You have been logged out.'})