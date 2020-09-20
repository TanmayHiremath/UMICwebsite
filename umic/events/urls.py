from django.urls import path, include

from .views import competitions_page

urlpatterns = [
	path('', competitions_page),
]
