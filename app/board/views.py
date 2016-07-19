from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from .models import Posts, Users
from form import UserForm

# Create your views here.
def index(request):
    post_list = Posts.objects.all()
    return render(request, 'index.html', {'post_list': post_list})


def createPost(request):
    return render(request, 'newPost.html')


def showPost(request, pk):
    post = Posts.objects.get(pk=pk)
    return render(request, 'postTemplate.html', {'post': post, })


def signUp(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        print userform
        # return redirect('index')
    else:
        userform = UserForm()
    return render(request, 'signUp.html', {'userform': userform, })