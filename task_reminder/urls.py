from django.urls import path, include
from .views import ToDoAPI


urlpatterns = [


    path('todo/', ToDoAPI.as_view()),
    # path('todo/<int:pk>/', ArticleDetail.as_view()),

]
