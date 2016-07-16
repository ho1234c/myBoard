from django.shortcuts import render
from .models import Posts


# Create your views here.
def index(request):
    print 'aabb'
    post_list = Posts.objects.all()
    return render(request, 'index.html', {'post_list': post_list})
