"""eg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

import django
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from entry.views import sgnup, logn
from django.conf.urls.static import static
from home.views import home

urlpatterns = [
    path('registration/',include('entry.urls')),
    path('guidee/',include('guidee.urls')),
    path('guide/',include('guide.urls')),
    path('chat/',include('chat.urls')),
    path('',home, name='home'),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)