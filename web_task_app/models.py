from django.urls import reverse

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email')
    bio = models.TextField(blank=True, max_length=500, verbose_name='biography')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='date of birth')


class Post(models.Model):
    theme = models.CharField(max_length=150, verbose_name='theme')
    content = models.TextField(verbose_name='content')
    photo = models.ImageField(upload_to='photos/', verbose_name='photo')
    active = models.BooleanField(default=True, verbose_name='is_active')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='date of publication')
    update_date = models.DateTimeField(auto_now=True, verbose_name='edit date')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'post_id': self.pk})

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'
        ordering = ['-create_date']


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='new', blank=True, null=True,
                             related_name='comments_posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='comment_author')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='date of comment')
    text = models.TextField(max_length=500, verbose_name='text of comment')
    active = models.BooleanField(default=True, verbose_name='is_active')

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ['-create_date']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.text, self.post)
