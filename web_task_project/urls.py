from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from web_task_app.views import ViewPosts, ViewUsers

router = SimpleRouter()
router.register('api/posts', ViewPosts)
router.register('api/users', ViewUsers)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_task_app.urls')),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
