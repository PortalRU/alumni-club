from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from register import views as v
from django.conf.urls.static import static

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('register/', v.register, name='register'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('articles.urls')),
    path('', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)