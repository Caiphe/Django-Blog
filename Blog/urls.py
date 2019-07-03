from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="Blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    # path('user/password_rest', UserPasswordResetView.as_view(),
    #  name="password-reset"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('about/', views.about, name="Blog-about")
]