from django.shortcuts import render,redirect
from accounts.forms import CustomUserCreationForm,CustomUserChangeForm,CustomUserChangeFormAdmin
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from accounts.models import User
from auctions.models import Winner
from auctions.views import winner
# Create your views here.


def singup(request):
    if not request.user.is_authenticated:    
        if request.method == 'POST':
            fm = CustomUserCreationForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'User Register Successfully ..!')
        else:
            fm = CustomUserCreationForm()

        return render(request, 'singup.html', {'form': fm})

    else:
        return redirect('login')

def logIn(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(request, username=uname, password=upass)
                if user is not None:
                    messages.success(request, 'Login successfully ..!')
                    login(request, user)
                    return redirect('login')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return redirect('dashbord')

def logOut(request):
    logout(request)
    return redirect('login')


def dashbord(request):
    winner(request)
    if request.user.is_authenticated:
        win = Winner.objects.all()
        u = 0
        data = User.objects.get(id=request.user.id)
        if request.user.is_superuser == True:
            u = 1
        return render(request, 'dashbord.html', {'name': request.user,'u':u,'user':data,'winner':win})
    else:
        return redirect('login')


def change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Password Change successfully ..!')
                update_session_auth_hash(request, fm.user)
                return redirect('dashbord')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'changepass.html', {'form': fm})
    else:
        return redirect('login')


def change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                print(fm.error_messages)
                fm.save()
                messages.success(request, 'Password Change successfully ..!')
                update_session_auth_hash(request, fm.user)
                return redirect('dashbord')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'changepass1.html', {'form': fm})
    else:
        return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        data = User.objects.get(id=request.user.id)
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = CustomUserChangeForm(request.POST,request.FILES,instance = data)
            else:
                fm = CustomUserChangeForm(request.POST,request.FILES,instance=data)
            if fm.is_valid():
                messages.success(request,'Profile Updated successfully..!')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = CustomUserChangeForm(instance=request.user)
            else:        
                fm = CustomUserChangeForm(instance=request.user)
        return render(request,'profile.html',{'form':fm,'data':data})    
    else:
        return redirect('login')



def all_user(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            users = User.objects.all()
            context = {
                'users':users
            }
            return render(request,'all_user.html',context)
        return redirect('login')


def user_del(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:

            pi = User.objects.get(id=id)
            fm = CustomUserChangeForm(instance=pi)

            context = {
                'form':fm
            }
            return render(request,'user_del.html',context)
        return redirect('login')