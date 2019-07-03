from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .models import Post
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

#forms
from .forms import PostForm
from .models import Post

#pagination
from django.core.paginator import Paginator


class PostsListView(ListView):
    template_name = 'board/listposts.html'
    context_object_name = 'posts_list'
    paginate_by = 15
    
    def get_queryset(self):
        return Post.objects.order_by('-date_published')

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name ='board/createpost.html'
    success_url = reverse_lazy('posts')

class PostDetailView(DetailView):
    model = Post
    template_name = 'board/detailpost.html'

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'board/updatepost.html'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'board/deleteview.html'
    success_url = reverse_lazy('posts')


