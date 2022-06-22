from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from rest_framework.viewsets import ModelViewSet

from .forms import UserRegisterForm, UserLoginForm, PostForm, AddCommentForm
from .models import Post, User, Comments
from .serializers import PostSerializer, UserSerializer
from rest_framework import generics
from . import serializers


class HomePosts(ListView):
    model = Post
    template_name = 'web_task_app/home.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home page'
        return context

    def get_queryset(self):
        return Post.objects.filter(active=True)


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'web_task_app/add_post.html'
    raise_exception = True

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


# detail Post + add comments
class ViewPost(DetailView, FormMixin):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'web_task_app/detail_post.html'
    context_object_name = 'post_item'
    form_class = AddCommentForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class AboutView(TemplateView):
    template_name = 'web_task_app/about.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('home')
        else:
            messages.error(request, "Registration error!")
    else:
        form = UserRegisterForm()
    return render(request, 'web_task_app/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'web_task_app/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


# rest api - view posts
class ViewPosts(ModelViewSet):
    queryset = Post.objects.filter(active=True)
    serializer_class = PostSerializer


# rest api - users
class ViewUsers(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# rest api - detail user
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
