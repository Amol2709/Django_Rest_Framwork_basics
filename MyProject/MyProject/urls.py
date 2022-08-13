"""MyProject URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from Post.views import PostView, post_list, post_detail, PostListView, DetailPostView, PostDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    #path('api/post-list/',post_list, name = 'post-list_function_based_view'),
    #path('api/post-list/',PostView.as_view(),name = 'post-list_class_ApiView'),
    #path('api/post-list/<int:pk>',PostView.as_view(),name = 'post-list_class_View'),
    #path('api/posts-list/',PostListView.as_view(),name = 'post-list_class_generic'),

    #path('api/posts/<int:pk>/',post_detail, name='post-detail_function'),
    #path('api/posts/<int:pk>/',PostView.as_view(), name='post-detail_function'),
    #path('api/posts/<int:pk>/',DetailPostView.as_view(),name = 'post-detail_class_ApiView'),
    path('api/posts/<int:pk>/',PostDetailView.as_view(),name = 'post-detail_class_generic_view')
    
]
