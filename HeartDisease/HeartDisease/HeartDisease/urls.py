"""
URL configuration for HeartDisease project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from signup.views import signaction
from login.views import loginaction

from .views import About, Contact, prediction, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signaction, name='signup'),  # Signup page
    path('login/', loginaction, name='login'),  # Login page
    path('contact/', Contact, name='contact'),
    path('about/', About, name='about'),
    path('predict/', prediction, name='prediction'),  # Prediction page
    path('', signaction),  # Redirect to signup page by default
    path('logout/', Logout, name='logout'),
]
