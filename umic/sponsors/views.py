from django.shortcuts import render
from .models import Sponsor

def sponsors_page(request):
    my_title = "Sponsors | UMIC, IIT Bombay"
    qs = Sponsor.objects.all()
    qss = []
    for i in range(0, qs.count(), 4):
    	ob = qs[i:i+4]
    	qss.append(ob)
    context = {"title": my_title, 'object_list_list': qss, "sponsors_active": "active"}
    return render(request, "sponsors/sponsors.html", context)

# Create your views here.
