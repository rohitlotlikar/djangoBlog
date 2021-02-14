"""my_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('travello/', include('travello.urls')),
    path('', include('blog.urls', namespace='blog')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # path('polls/', include('polls.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
