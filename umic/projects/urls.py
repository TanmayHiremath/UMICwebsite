from django.urls import path, include

from .views import projects_page

urlpatterns = [
	path('', projects_page),
]
