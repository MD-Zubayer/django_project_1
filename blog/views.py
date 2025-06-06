from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import SigninForm

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