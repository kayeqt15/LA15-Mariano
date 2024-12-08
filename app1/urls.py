from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),       # Example URL inside app1
    path('hi/', views.say_hi),             # Another example URL
    path('posts/', views.blog_list, name="blog_list"),  # To list posts
    path('posts/<int:id>/', views.blog_detail, name="blog_detail"),  
]
