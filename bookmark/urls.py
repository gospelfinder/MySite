from django.urls import path
from bookmark import views


app_name = 'bookmark' # 네임스페이스 
urlpatterns = [
    # mvc ==> mvt : m - model, v - controller, t - view
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
    path('add/', views.BookmarkCreateView.as_view(), name="add",),
    path('change/', views.BookmarkChangeLV.as_view(), name="change",),
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name="update",),
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name="delete",),
]

