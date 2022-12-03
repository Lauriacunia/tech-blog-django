from django.views import View 
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.shortcuts import redirect, render
from candycode.settings import LOGIN_URL
from post.models import Post
from .forms.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

class PostList(ListView):
    model = Post
    template_name = 'base_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by: int = 3
    

    def get(self, request, *args, **kwargs):

        if request.GET.get('search'):
            filtered_posts = Post.objects.filter(title__icontains=request.GET.get('search')).order_by('-date_posted')
            if filtered_posts:
                 return render(request, 'base_posts.html', {'posts': filtered_posts, 'is_filtered': True})
            else:
                messages.error(request, 'Sorry, No posts found')
                return render(request, self.template_name, {'posts': Post.objects.all().order_by('-date_posted')})
           
        else:
            return super().get(request, *args, **kwargs)

    

class SearchPostByName(ListView):
    def get_queryset(self):
        post_title = self.request.GET.get('post-title')
        return Post.objects.filter(title__icontains=post_title)

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'write.html'
    form_class = PostForm
    login_url: 'LOGIN_URL'

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})
        
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        user = request.user
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
            
            return redirect('all_posts')
        return render(request, self.template_name, {'form': form})



class MyPostList(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'my_account.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    login_url: 'LOGIN_URL'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-date_posted')

class EditPost(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'edit.html'
    form_class = PostForm
    context_object_name = 'post'
    login_url: 'LOGIN_URL'


    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(instance=post)
        return render(request, self.template_name, {'form': form, 'post': post})
        
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('all_posts')
        return render(request, self.template_name, {'form': form, 'post': post})
    

class DeletePost(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy("all_posts")
    login_url: 'LOGIN_URL'

class DetailPost(DetailView):
    model= Post
    template_name: str = 'detail.html'