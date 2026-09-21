from django.urls import path
from .views import (home, post_list, post_detail, post_create, post_update, post_delete, add_comment, category_posts, category_list) 

urlpatterns = [
    path('', home, name='home'),
    path('posts/', post_list, name='post_list'),
    path('posts/<slug:slug>/', post_detail, name='post_detail'),
    path('categories/<slug:slug>/', category_posts, name='category_posts'),
    path('posts/create/', post_create, name='post_create'),
    path('posts/<int:id>/edit/', post_update, name='post_update'),
    path('posts/<int:id>/delete/', post_delete, name='post_delete'),
    path('posts/<int:post_id>/comment/', add_comment, name='add_comment'),
    path('categories/', category_list, name='category_list'),
]