from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProfileView, CustomAuthToken

urlpatterns = [
    path('profile/', ProfileView.as_view()),
    path('api/authToken/', CustomAuthToken.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)