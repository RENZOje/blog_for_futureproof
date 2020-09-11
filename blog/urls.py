from django.urls import path, include
from .views import *






urlpatterns = [

    path('', PostView.as_view(), name='home'),
    path('tag/', TagPostView.as_view(), name='tag'),
    path('tag/<str:slug>', TagPostView.as_view(), name='detail_tag'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='detail_post'),

]
