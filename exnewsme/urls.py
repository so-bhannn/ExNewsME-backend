"""
URL configuration for exnewsme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from news import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
   path('admin/', admin.site.urls),
   path('news/', views.NewsArticleListView.as_view(), name='news-list'),
   path('news/<int:pk>/', views.NewsArticleDetailView.as_view(), name='news-detail'),
   path('news/create/', views.NewsArticleCreateView.as_view(), name='news-create'),
   path('news/<int:pk>/update/', views.NewsArticleUpdateView.as_view(), name='news-update'),
   path('login/', views.CustomAuthToken.as_view()),
   path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
