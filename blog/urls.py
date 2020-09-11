from django.urls import path, include
from .views import *






urlpatterns = [

    path('', MainView.as_view(), name='home'),
    path('tag/<str:slug>', TagPostView.as_view(), name='detail_tag'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='detail_post'),

]
