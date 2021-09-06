from django.urls import path
from .views import *
from . import api 
from .views import ListThreads, CreateThread, CreateMessage
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>', CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('search/', SearchUser.as_view(), name='profile-search'),

    ### api endpoints for profiles
    path('api/profile/', api.ProfileList.as_view(), name='profile-api'),
    path('api/profile/<int:pk>/', api.ProfileDetails.as_view(), name='profile-detail-api'),
    
    ### api endpoints for posts
    path('api/post/', api.PostList.as_view(), name='post-api'),
    path('api/post/<int:pk>/', api.PostDetails.as_view(), name='post-detail-api'),
    
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread/', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),

    ### chat room
    # path('<str:roomname>/', views.room, name='room'),
]
    