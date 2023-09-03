from django.urls import path
from . import views

urlpatterns = [
    path('',views.articlesListView.as_view(),name='articleListPage'),
    path('cat/<str:category>',views.articlesListView.as_view(),name='articleByCategoryListPage'),
    path('<pk>/', views.articleDetailView.as_view(), name='articleDetailPage'),
    path('add-article-comment', views.addArticleComment, name='add-article-comment'),

]
