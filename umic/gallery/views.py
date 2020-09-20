from django.shortcuts import render
from .models import Image 

def gallery_page(request):
	my_title = "Gallery | UMIC IIT Bombay"
	template = "gallery/gallery.html"
	achieve = Image.objects.all()[10:25]
	team = Image.objects.all()[0:10]
	robo = Image.objects.all()[25:43]
	misc = Image.objects.all()[43:55]
	context = {"title": my_title, "achieve":achieve, "team":team, "robo":robo, "misc":misc, "gallery_active": "active"}
	return render(request, template, context)

# Create your views here.
def gallery_intro(request):
	my_title = "Gallery | UMIC IIT Bombay"
	template = "gallery/intro.html"
	context = {"title": my_title}
	return render(request, template, context)
