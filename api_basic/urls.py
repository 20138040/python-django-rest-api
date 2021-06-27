from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from .views import article_view, article_detail, ArticleList, ArticleDetail, GenericArticle, ArticleViewSet


router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='articles')

urlpatterns = [

    path('viewset/', include(router.urls)),

    path('articles/', article_view),
    path('articles/<int:pk>/', article_detail),

    path('articles2/', ArticleList.as_view()),
    path('articles2/<int:pk>/', ArticleDetail.as_view()),

    path('generic/articles/', GenericArticle.as_view()),
    path('generic/articles/<int:id>/', GenericArticle.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)