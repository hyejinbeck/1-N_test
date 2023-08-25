from django.urls import path 
from . import views 

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('<int:id>/', views.detail, name='detail'),
    
    path('create/', views.create, name ='create'),

    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),

    path('<int:article_id>/comments/delete/<int:id>/', views.delete_comment, name='delete_comment'),
]