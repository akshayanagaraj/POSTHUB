
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home-url'),
    path('about/',views.about, name='about-url'),
    path('myposts/',views.all_posts, name='my-posts-url'),
    path('createpost/', views.create_post, name='createpost-url'),
    path('myposts/<int:id>', views.detail, name='detail-url'),

]
