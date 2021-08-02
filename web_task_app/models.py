from django.urls import reverse

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email')
    bio = models.TextField(blank=True, max_length=500, verbose_name='Биография')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')


class Post(models.Model):
    theme = models.CharField(max_length=150, verbose_name='Тема поста')
    content = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото')
    active = models.BooleanField(default=True, verbose_name='Активно')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'post_id': self.pk})

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-create_date']


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', blank=True, null=True,
                             related_name='comments_posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')
    text = models.TextField(max_length=500, verbose_name='Текст комментария')
    active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-create_date']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.text, self.post)
