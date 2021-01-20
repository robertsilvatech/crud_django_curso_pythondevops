"""pastelariaDevops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls import include
from .views import hello
from .views import mymachine
from .views import healthcheck
from pastelariaDevops.core import urls as core_url

urlpatterns = [
    path('healthcheck', healthcheck),
    path('mymachine', mymachine),
    path('hello', hello),
    path('admin/', admin.site.urls),
    path('loja/', include(core_url))
]
