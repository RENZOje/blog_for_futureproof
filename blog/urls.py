from django.urls import path, include
from .views import *

urlpatterns = [

    path('', MainView.as_view(), name='home'),
    path('draft_post', DraftPostView.as_view(), name='draft_post'),
    path('tag/<str:slug>', TagPostView.as_view(), name='detail_tag'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='detail_post'),

    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),

    path('create_post/<str:pk>/', create_post, name='create_post'),
    path('update_post/<str:pk>/', update_post, name='update_post'),
    path('delete_post/<str:pk>/', delete_post, name='delete_post'),
]
