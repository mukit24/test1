from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def home_index(request):
    msgs = Post.objects.all()
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_index')
    return render(request,"home/index.html",{'msgs':msgs,'form':form})