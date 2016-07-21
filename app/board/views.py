from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Posts, Users, Categories
from form import UserForm

# Create your views here.
def index(request):
    post_list = reversed(Posts.objects.all())
    return render(request, 'index.html', {'post_list': post_list})


def createPost(request):
    if request.method == 'POST':
        user = Users.objects.get(name=request.session['username'])
        category = Categories.objects.get(pk=1)
        post = Posts.objects.create(title=request.POST['title'], content=request.POST['content'], user=user, category=category)
        # post.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'newPost.html')


def showPost(request, pk):
    post = Posts.objects.get(pk=pk)
    return render(request, 'postTemplate.html', {'post': post, })


def signUp(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        userform = UserForm()
    return render(request, 'registration/signUp.html', {'userform': userform, })


def signIn(request):
    if request.method == 'POST':
        user = Users.objects.get(name=request.POST['username'])
        if user.password == request.POST['password']:
            request.session['username'] = user.name
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'registration/login.html')


def logout(request):
    del request.session['username']
    return HttpResponseRedirect(reverse('index'))
