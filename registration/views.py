from django.shortcuts import render, HttpResponseRedirect,redirect
from registration.forms import RegistrationFrom,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User

# Create your views here.


def singup(request):
    if not request.user.is_authenticated:    
        if request.method == 'POST':
            fm = RegistrationFrom(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'User Register Successfully ..!')
        else:
            fm = RegistrationFrom()

        return render(request, 'singup.html', {'form': fm})

    else:
        return redirect('profile')

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
                    return HttpResponseRedirect('/profile/')

        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return redirect('profile')

def logOut(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def profile(request):
    if request.user.is_authenticated:
        u = 0
        if request.user.is_superuser == True:
            u = 1
        return render(request, 'profile.html', {'name': request.user,'u':u})
    else:
        return HttpResponseRedirect('/login/')


def change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Password Change successfully ..!')
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


def change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                print(fm.error_messages)
                fm.save()
                messages.success(request, 'Password Change successfully ..!')
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'changepass2.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')

def profile_edit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST,instance=request.user)
            else:
                fm = EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,'Profile Updated successfully..!')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
            else:        
                fm = EditUserProfileForm(instance=request.user)
        return render(request,'profileEdit.html',{'form':fm})    
    else:
        return HttpResponseRedirect('/login/')



def all_user(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            users = User.objects.all()
            context = {
                'users':users
            }
            return render(request,'all_user.html',context)
        return HttpResponseRedirect('/login/')

def user_del(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:

            pi = User.objects.get(id=id)
            fm = EditAdminProfileForm(instance=pi)

            context = {
                'form':fm
            }
            return render(request,'user_del.html',context)
        return HttpResponseRedirect('/login/')