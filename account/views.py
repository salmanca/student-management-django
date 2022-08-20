from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from students.models import StudentModel


def user_login(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            messages.success(request, 'Invalid Credetials')
            return redirect('login')
    else:
        return render(request, 'account/login_page.html')

def user_register(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']
        try:
            keep_logedin = request.POST['keep_loged']
        except:
            keep_logedin = None
        if password == password1:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                    user.save()
                    if keep_logedin == "true":
                        auth.login(request, user)
                        messages.success(request, 'loged in successfully')
                        return redirect('dashboard')
                    else:
                        messages.success(request, 'Registered successfully')
                        return redirect('login')
                else:
                    messages.error(request, 'Email already exists')
                    return redirect('register')
            else:
                messages.error(request, 'Username already exists')
                return redirect('register')
        else:
            messages.error(request, 'Password does not match')
            return redirect('register')
    return render(request, 'account/register_page.html')

@login_required(login_url = 'login')
def dashboard(request):
    user = request.user.id
    students = StudentModel.objects.filter(admin=user)
    context = {
        "students" : students
    }
    return render(request, 'account/dashboard.html', context)

def user_logout(request):
    auth.logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('login')
