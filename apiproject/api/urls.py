# from django.contrib import admin
# from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
urlpatterns = [
    # path('articles/', article_list),
    # path('articles/<int:pk>/', article_details),
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:id>/', ArticleDetails.as_view())
    path('', include(router.urls)),
    
]
