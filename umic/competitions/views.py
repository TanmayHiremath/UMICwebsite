from django.shortcuts import render

def competitions_page(request):
	print(request)
	my_title = "Competitions | UMIC IIT Bombay"
	template = "competitions/competitions.html"
	context = {"title": my_title, "competitions_active": "active"}
	return render(request, template, context)

# Create your views here.
def asme_page(request):
	if request.path == '/competitions/ASME':
		return render(request, 'competitions/asme.html', {'title':'ASME | UMIC IIT Bombay', "competitions_active": "active"})
	elif request.path == '/competitions/AeRoVe':
		return render(request, 'competitions/aerove.html', {'title':'AeRoVe | UMIC IIT Bombay', "competitions_active": "active"})
	elif request.path == '/competitions/SeDriCa':
		return render(request, 'competitions/sedrica.html', {'title':'SeDriCa | UMIC IIT Bombay', "competitions_active": "active"})		
	elif request.path == '/competitions/others':
		return render(request, 'competitions/others.html', {'title':'Others | UMIC IIT Bombay', "competitions_active": "active"})
		