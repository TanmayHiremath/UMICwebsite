from django.urls import path, include
from .views import current_team_page, past_team_page

urlpatterns = [
	path('current/', current_team_page, name='current_team_page'),
	path('past/', past_team_page, name='past_team_page'),
]