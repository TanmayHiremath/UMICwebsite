from django.shortcuts import render
from .models import Project

def projects_page(request):
	my_title = "Projects | UMIC IIT Bombay"
	template = "projects/projects.html"
	qs = Project.objects.all()
	qss = []
	for i in range(0, qs.count(), 2):
		ob = qs[i:i+2]
		qss.append(ob)
	context = {"title": my_title, "obj_list": qss, "projects_active": "active"}
	return render(request, template, context)
# Create your views here.
