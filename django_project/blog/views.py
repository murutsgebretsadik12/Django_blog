from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
) 




# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['date_posted']

class PostDetailView(DetailView):
    model = Post  
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  
    
    #Overriding form_valid method 
    def form_valid(self, form):
        form.instance.author = self.request.user # Set the author on the form
        return super().form_valid(form) # Validate form by running form_valid method from parent class.
 
 
class PostUpdateView(LoginRequiredMixin, UpdateView): # New class created and UpdateView passed in.
    model = Post
    fields = ['title', 'content']
     
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # New class PostDeleteView created here
    model = Post
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
 
    
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    