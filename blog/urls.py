from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('sort/', views.Sort.as_view(), name='sort'),
    path('Search/', views.Search.as_view(),name='search'),

    path('register/',views.register,name='register')]
