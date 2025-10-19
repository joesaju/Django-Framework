from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    return render(request, 'register.html')

def dashboard(request):
    return render(request, 'predictions/dashboard.html')

def spam_predict(request):
    prediction = ""
    if request.method == 'POST':
        text = request.POST['text']
        if "free" in text.lower() or "win" in text.lower():
            prediction = "Spam Message 🚫"
        else:
            prediction = "Not Spam ✅"
    return render(request, 'predictions/spam_predict.html', {'prediction': prediction})

def house_rent_predict(request):
    rent = None
    if request.method == 'POST':
        sqft = int(request.POST['sqft'])
        bhk = int(request.POST['bhk'])
        location_score = int(request.POST['location'])
        rent = (sqft * 15) + (bhk * 5000) + (location_score * 1000)
    return render(request, 'predictions/house_rent.html', {'rent': rent})

def pension_predict(request):
    pension = None
    if request.method == 'POST':
        age = int(request.POST['age'])
        salary = int(request.POST['salary'])
        pension = round((salary * (60 - age) * 0.1), 2)
    return render(request, 'predictions/pension.html', {'pension': pension})

def logout_view(request):
    logout(request)
    return redirect('login')

