from django.urls import path, include

from .views import *

urlpatterns = [
	path('', competitions_page),
	path('ASME',asme_page),
	path('AeRoVe',asme_page),
	path('SeDriCa',asme_page),
	path('others',asme_page)
]
