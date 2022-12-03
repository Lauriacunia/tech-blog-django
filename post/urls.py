from django.contrib import admin
from django.urls import path
from post.views import PostList, CreatePost, MyPostList, EditPost, DetailPost, SearchPostByName, DeletePost

urlpatterns = [
    path('', PostList.as_view(), name='all_posts'),
    path('new-post/', CreatePost.as_view(), name='new_post'),
    path('my-account/', MyPostList.as_view(), name='my_account'),
    path('edit-post/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('delete-post/<int:pk>/', DeletePost.as_view(), name='delete_post'),
    path('detail-post/<int:pk>/', DetailPost.as_view(), name='detail_post'),
]