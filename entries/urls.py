from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detail/<int:id>', views.detail),
    path('add_post/', views.add_post),
    path('like/<int:id>', views.like_post),
]

#ath('', views.index),
#path('add_todo/', views.add_todo),
#path('delete_todo/<int:todo_id>/', views.delete_todo),