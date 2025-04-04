from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login


User = get_user_model()


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        gender = request.POST.get('gender')
        username = request.POST.get('username')
        password = request.POST.get('password')


        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'data': 'Username already taken!'})


        user = User.objects.create_user(username=username, password=password, email=email)
        user.full_name = full_name  
        user.contact_no = contact_no
        user.gender = gender
        user.save()

        return redirect('student_home')

    return render(request, 'register.html')

# Login Page
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_home')
        else:
            return render(request, 'login.html', {'data': 'Invalid username or password'})

    return render(request, 'login.html')

# Student Home Page
def student_home(request):
    return render(request, 'studenthome.html', {'data': 'Welcome to your dashboard!'})

def student_view(request):
    return render(request, 'student.html')