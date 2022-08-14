from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyBlogList.as_view(), name="home"),
    path('details/<str:pk>/', views.MyBlogDetails.as_view(), name="blog-details"),
    path('create-blog/', views.CreateNewBlog.as_view(), name="create-blog"),
    path('update-blog/<str:pk>/', views.UpdateBlog.as_view(), name="update-blog"),
    path('delete-blog/<str:pk>/', views.DeleteBlog.as_view(), name="delete-blog"),
]
