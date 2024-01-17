from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "starting-page"),
    path('posts/',views.posts, name = "posts-page"),
    path('posts/<slug:slug>',views.individual_post, name = "post-details")
]
