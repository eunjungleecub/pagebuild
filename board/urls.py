from django.urls import path
from . import views
from .views import PostsListView, PostCreateView, PostDetailView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('', PostsListView.as_view(), name='posts'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
]