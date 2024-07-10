from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse 
from django.contrib.auth.mixins import  LoginRequiredMixin,PermissionRequiredMixin
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

def home(request):
	context={
      'posts':Post.objects.all()
	}
	return render(request,'blog/Home.html',context)

class PostListView(ListView):
	model=Post
	template_name='blog/Home.html'
	context_object_name='posts'
	ordering=['-date_posted']
	paginate_by=4


class PostDetailView(DetailView):
	model=Post

class PostCreateView(LoginRequiredMixin,CreateView,PermissionRequiredMixin):
    permission_required='is_superuser'
    success_url='/'
    model=Post
    fields=['title','content']

class PostUpdateView(UpdateView,PermissionRequiredMixin):
    permission_required='is_superuser'
    model=Post
    success_url='/'
    fields=['title','content']

class PostDeleteView(DeleteView,PermissionRequiredMixin):
    permission_required='is_superuser'
    model=Post
    success_url='/'

def about(request):
	return render(request,'blog/about.html',{'title': 'About'})



