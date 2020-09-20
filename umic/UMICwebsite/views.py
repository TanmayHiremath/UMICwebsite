from django.http import HttpResponse
from django.shortcuts import render
from events.models import Announcement, Event
from sponsors.models import Sponsor

def home_page(request):
	my_title = "Home | UMIC, IIT Bombay"
	qs = Sponsor.objects.all()
	qss = []
	for i in range(0, qs.count(), 4):
		ob = qs[i:i+4]
		qss.append(ob)
	events = Event.objects.all()[:2]
	announcements = Announcement.objects.all()[:2]
	context = {"title": my_title, "events": events, "announcements": announcements, 'object_list_list': qss, 'home_active': "active"}
	return render(request, "home.html", context)