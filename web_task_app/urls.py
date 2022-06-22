from django.urls import path
from .views import register, user_logout, user_login, HomePosts, CreatePost, ViewPost, AboutView, UserDetail

urlpatterns = [
    path('', HomePosts.as_view(), name='home'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('about/', AboutView.as_view(), name='about'),
    path('posts/add-post/', CreatePost.as_view(), name='add_post'),
    path('post/<int:post_id>/', ViewPost.as_view(), name='detail_post'),
    path('users/<int:pk>/', UserDetail.as_view()),
]
