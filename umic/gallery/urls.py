from django.urls import path

from .views import gallery_page, gallery_intro

urlpatterns = [
	path('', gallery_page),
	path('intro', gallery_intro)
]