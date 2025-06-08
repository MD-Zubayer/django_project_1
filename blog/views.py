from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import SigninForm, SiginUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def signin_view(request):
    form = SigninForm(request.POST or None)
    data = {}
    err = {}

    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
        else:
            err = form.errors

    return render(request, 'blog/signin.html', {'form': form, 'data': data, 'err': err})

def signUp_view(request):


    return render(request, 'blog/sign-up.html', {})

def profile_view(request):
    return render(request, 'blog/profile.html', {})

def index2(request):
    return render(request, 'blog/index2.html', {})

# def UserSignUp_view(request):
#     if request.method == 'POST':
#         form = SiginUpForm(request.POST)
#         if form.is_valid():
#             # cleaned data
#             user_name = form.cleaned_data['user_name']
#             phone_number = form.cleaned_data['phone_number']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             # Save the user data to the database
#             contact = contact(user_name=user_name, phone_number=phone_number, email=email, password=password)
#             contact.save()
#             return redirect('profile')
            
#         else:
#             return render(request, 'blog/sign-up.html', {'form': form, 'errors': form.errors})
#     else:
#         form = SiginUpForm()
#     return render(request, 'sign-up.html', {form:form})
        

def UserSignUp_view(request):
    if request.method == 'POST':
        form = SiginUpForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            username = form.cleaned_data['username']
            phone_number = form.cleaned_data.get('phone_number')  # handle optional phone
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            # Create user with hashed password
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            # Optionally store extra profile info
            # if phone_number:
            #     user.profile.phone_number = phone_number
            #     user.profile.save()

            # Log the user in immediately
            login(request, user)

            messages.success(request, "Your account has been created successfully.")
            return redirect('profile')
        else:
            # Form invalid: render with errors
            return render(request, 'blog/sign-up.html', {'form': form})
    else:
        form = SiginUpForm()

    return render(request, 'blog/sign-up.html', {'form': form})
