from django.shortcuts import render

def contact_page(request):
	template_name = "contact/contact.html"
	title = "Contact Us | UMIC IIT Bombay"
	context = {"title": title, "contact_active": "active"}
	return render(request, template_name, context)

# Create your views here.
