from django.urls import path

from .views import (
    home,
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
    add_comment,
    category_posts,
    category_list,
    search_posts,
)

from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('', home, name='home'),

    path('posts/', post_list, name='post_list'),

    # CREATE va boshqa maxsus URL'lar
    # slug URL'dan OLDIN turishi kerak
    path('posts/create/', post_create, name='post_create'),

    path(
        'posts/<int:id>/edit/',
        post_update,
        name='post_update'
    ),

    path(
        'posts/<int:id>/delete/',
        post_delete,
        name='post_delete'
    ),

    path(
        'posts/<int:post_id>/comment/',
        add_comment,
        name='add_comment'
    ),

    # slug URL oxirroqda
    path(
        'posts/<slug:slug>/',
        post_detail,
        name='post_detail'
    ),

    path(
        'categories/<slug:slug>/',
        category_posts,
        name='category_posts'
    ),

    path(
        'categories/',
        category_list,
        name='category_list'
    ),

    path(
        'search/',
        search_posts,
        name='search_posts'
    ),

    path(
        'logout/',
        LogoutView.as_view(next_page='home'),
        name='logout'
    ),
]