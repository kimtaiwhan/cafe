from django.urls import path
from . import views

urlpatterns = [
    path('', views.signIn, name="signIn"),
    path('postsignIn/', views.postsignIn, name='postsignIn'),
    path('signUp/', views.signUp, name='signUp'),
    path('postsignUp/', views.postsignUp, name='postsignUp'),
    path('logout/', views.logout, name='logout'),
    path('main/', views.main, name='main'),
    path('chart/', views.chart, name='chart'),
    path('review/', views.review, name="review"),
    path('test/', views.test, name='test'),
]   