"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('comment/', include('comment.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('', views.home, name = 'home'),
    path('login/', views.login, name = 'login' ),
    path('logout/', views.logout, name = 'logout' ),
    path('register/', views.register, name = 'register' ),
    path('user_info/', views.user_info, name = 'user_info' ),
    path('game/', include('game.urls')),
    path('login/login_by_qq', views.login_by_qq, name = 'login_by_qq' ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
