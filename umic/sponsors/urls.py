from django.urls import path, include

from .views import sponsors_page

urlpatterns = [
	path('', sponsors_page),
]
