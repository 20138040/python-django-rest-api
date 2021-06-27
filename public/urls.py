from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PublicView

urlpatterns = [
    path('', PublicView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)