from django.shortcuts import render
from .models import Event, Image

def competitions_page(request):
	my_title = "Events | UMIC IIT Bombay"
	template = "events/events.html"
	objects = Event.objects.all()
	dict = {}
	for obj in objects:
		images = obj.event.all()
		dict[obj] = images
	context = {"title": my_title, "events": dict, "events_active": "active"}
	return render(request, template, context)
# Create your views here.
