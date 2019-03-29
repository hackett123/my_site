"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from core.views import splash, about_me, teaching, music, projects, career

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash, name="splash"),
    path('about_me/', about_me, name="about_me"),
    path('teaching/', teaching, name="teaching"),
    path('music/', music, name="music"),
    path('projects/', projects, name="projects"),
    path('career/', career, name="career")
]
