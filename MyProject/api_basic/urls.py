from django.urls import path
from .views import article_list, article_detail, ArticleAPIVIew


urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleAPIVIew.as_view()),
    path('detail/,<int:pk>/', article_detail),
]
