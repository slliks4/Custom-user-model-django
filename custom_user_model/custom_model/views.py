from django.shortcuts import render,redirect
from .models import Account
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

def home(request):
    accounts = Account.objects.all()
    return render(request,'index.html',{'accounts':accounts})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']    
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return render(request, 'login_successful.html')
            else:
                messages.info(request, 'invalid login details')
                return redirect('login')
        else:
            return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']

            def validate_email(email):
                email_validator = EmailValidator()

                try:
                    email_validator(email)
                    return True
                
                except ValidationError:
                    return False
                
            email_is_valid = validate_email(email)
            
            if email_is_valid:
                if len(password)>8:
                    if password == password2:
                        if Account.objects.filter(email=email).exists():
                            messages.info(request, 'email already exists')
                            return redirect('user_signup')
                        elif Account.objects.filter(username=username).exists():
                            messages.info(request, 'username already exists')
                            return redirect('user_signup')
                        else:
                            user = Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password,birth_day=None)
                            user.save()
                            return render(request, 'signup_success.html')
                    else:
                        messages.info(request,'password mismatch')
                        return redirect('user_signup')
                else:
                    messages.info(request,'password must be more than 8 characters')
                    return redirect('user_signup')
                
            else:
                messages.info(request, 'invalid email address')
                return redirect('user_signup')                
        
        else:
            return render(request, 'signup.html')


