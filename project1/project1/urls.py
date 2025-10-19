"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app1 import views as v1 #to avoid overwriting, use aliases to avoid error.because python accepts the latest imported package
from app2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("x/", v1.xyz),
    path("welcome/", views.welcome),
    path("a/", views.one),
    path("b/", views.two),
    path("c/",views.three),
    path("d/",views.time),
    path("emp/",views.emp),
]

