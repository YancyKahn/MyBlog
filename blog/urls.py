from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('blog/index', views.IndexView.as_view(), name='index'),
    path('blog/search/', views.SearchListView.as_view(), name='search'),
    path('blog/detail/<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
    path('blog/like/', views.like, name='like'),
    path('blog/collect/', views.collect, name='collect'),
]
