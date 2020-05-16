"""x1coder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework_jwt.views import obtain_jwt_token
from users.views import RegisterUserView, LoginUserView

urlpatterns = [
    #path('admin/', admin.site.urls),
    # path('v1/login',LoginUserView.as_view(),name='login'),
    path('v1/login',obtain_jwt_token,name='login'),
    path('v1/register',RegisterUserView.as_view(),name='register'),
    path('v1/users',include('users.urls')),
    path('v1/challegen',include('challegen.urls')),
]

