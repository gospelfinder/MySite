from django.urls import path, re_path
from board import views

app_name = 'board'
urlpatterns = [
    path('', views.BoardLV.as_view(), name='index'),
    
    path('board/', views.BoardLV.as_view(), name='board_list'),

    re_path(r'^board/(?P<slug>[-\w]+)/$', views.BoardContentView.as_view(), name="board_detail"),
    
    path('add/', views.BoardCreateView.as_view(), name="add",),
    
    path('change/', views.BoardChangeLV.as_view(), name="change",),
    
    path('<int:pk>/update/', views.BoardUpdateView.as_view(), name="update",),

    path('<int:pk>/delete/', views.BoardDeleteView.as_view(), name="delete",),
    
]