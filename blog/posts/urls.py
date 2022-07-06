from django.urls import path
from .views import HomeView,ArticleDetailView,PostCreateView,UpdatePostView,DeletePostView,CategoryCreateView,CategoryView

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('article/<int:pk>/',ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', PostCreateView.as_view(),name = 'add_post'),
    path('article/edit/<int:pk>/',UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete',DeletePostView.as_view(), name='delete_post'),
    path('add_category/', CategoryCreateView.as_view(),name = 'add_category'),
    path('category/<str:cats>/', CategoryView,name='category')
]
