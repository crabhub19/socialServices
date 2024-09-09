from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from .models import *
import os

# Create your views here.

# it is index page-----------------------------------------------------------
def index(request):
    worker = Worker.objects.all()
    return render(request,'index.html',{'worker':worker})

# it is signup code------------------------------------------------
def signup(request):
    district = District.objects.all()
    worker = Worker.objects.all()
    contex ={
        'district':district,
        'worker':worker
    }
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            # Create the user
            try:
                # Continue with user creation logic
                user = User.objects.create_user(username=username, first_name=first_name, password=password)
                user.save()
            except IntegrityError:
                # Handle the case where the username is already taken
                # You may want to return an error message to the user
                messages.error(request,"Username already taken, please choose another.")
                return redirect('signup')

            # Create the user profile
            localAddress = request.POST['localAddress']
            contracNo = request.POST['contracNo']
            gender = request.POST['gender']
            district_id=request.POST.get("district")
            district = District.objects.get(pk=district_id)
            worker_id=request.POST.get("worker")
            worker = Worker.objects.get(pk=worker_id)
            userImage = request.FILES.get('userImage', None)

            userss = Users(user=user,localAddress=localAddress, contracNo=contracNo, gender=gender, district=district, worker=worker, userImage=userImage)
            userss.save()

            login(request, user)
            messages.success(request,"your have successfully created your account")
            return redirect('/')  # Redirect to the home page after successful signup
        else:
            messages.error(request,"your password and confirm password is not same")
            return redirect('signup')

    return render(request, 'signup.html',contex)





def worker(request,name):
    district = District.objects.all()
    users = Users.objects.filter(active=True)
    print(name)
    

    return render(request,'worker.html',{'users':users,'name':name,'district':district})


# profile__________________________________________________________________
@login_required(login_url='user_login')
def profile(request):
    profile = Users.objects.get_or_create(user=request.user)[0]
    return render(request,'profile.html',{'profile':profile})



# login---------------------------------------------------------------------
def userlogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # if user.is_active:
            #     request.session.set_expiry(86400)
            #     request.session['user_id'] = user.id
            messages.success(request,"confirm that you are one of us")
            return redirect('/')
        else:
            messages.error(request,"username or password was worng")
            return redirect('userlogin')
    return render(request,'login.html')

# logout_________________________________________________________________________
def userlogout(request):
    logout(request)
    messages.success(request,"logout successfully")
    return redirect('/')

@login_required
def delete_account(request, username):
    profile = Users.objects.get_or_create(user=request.user)[0]
    if len(profile.userImage)>0:
        image_path = profile.userImage.path
        if os.path.exists(image_path):
            os.remove(image_path)
        profile.userImage.delete()
    # profile.delete()

    user = get_object_or_404(User, username=username)
    user.delete()

    messages.success(request,"delete successfully")
    return redirect('/')  # Redirect to your logout view


@login_required
def active_account(request,username):
    profile = Users.objects.get_or_create(user=request.user)[0]
    profile.active=True
    profile.save()
    return redirect('profile')

@login_required
def deactive_account(request,username):
    profile = Users.objects.get_or_create(user=request.user)[0]
    profile.active=False
    profile.save()
    return redirect('profile')


@login_required
def update_contract_user(request):
    if request.method == 'POST':
        new_contracNo = request.POST.get('contracNo')
        # new_userImage = request.FILES.get('userImage')
        
        profile = Users.objects.get_or_create(user=request.user)[0]
        if new_contracNo:
            profile.contracNo=new_contracNo
            profile.save()
            messages.success(request, 'your contract information has been updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'your have not enter any information.')
            return redirect('profile')
        
@login_required
def update_userImage_user (request):
    if request.method == 'POST':
        new_userImage = request.FILES.get('userImage')
        
        profile = Users.objects.get_or_create(user=request.user)[0]
        if new_userImage:
            if len(profile.userImage)>0:
                image_path = profile.userImage.path
                if os.path.exists(image_path):
                    os.remove(image_path)
                profile.userImage.delete()
            profile.userImage = new_userImage
            profile.save()
            messages.success(request, 'your image has been updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'your have not been added any image.')
            return redirect('profile')
        


@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user

        # Check if the current password is correct
        if not user.check_password(current_password):
            messages.error(request, 'Invalid current password.')
            return redirect('profile')

        # Check if the new password and confirmation match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirmation do not match.')
            return redirect('profile')

        # Change the user's password
        user.set_password(new_password)
        user.save()

        # Update the session to prevent logouts
        update_session_auth_hash(request, user)

        messages.success(request, 'Your password was successfully updated!')
        return redirect('profile')  # Redirect to the user's profile page
