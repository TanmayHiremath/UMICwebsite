from django.shortcuts import render
from django.http import Http404
from .models import (
	CurrentTeam,
	OC,
	TeamMember,
	StudentAdvisor,
	Faculty,
	PastTeam,
	PastOC,
	NotableAlumni,
	)

def current_team_page(request):
	template_name = "team/current_team.html"
	current_team = CurrentTeam.objects.all()[0]
	oc = current_team.oc.all()
	tm1 = current_team.member.all()[:2]
	tm = current_team.member.all()[2:]
	sa = current_team.advisor.all()
	fac = current_team.faculty.all()
	context = {"title": "Team | UMIC IIT Bombay", "ct": current_team, "current_active": "active", "oc": oc, "tm": tm, "tm1":tm1, "sa": sa, "fac": fac, "team_active": "active"}
	return render(request, template_name, context)

def past_team_page(request):
	template_name = "team/past_team.html"
	current_team = CurrentTeam.objects.all()[0]
	gp = current_team.group_photo
	past_team = PastTeam.objects.all()[0]
	past_oc = past_team.past_oc.all()
	na = past_team.notable_alumni.all()
	context = {"title": "Team | UMIC IIT Bombay", "ct": current_team, "past_active": "active", "past_oc": past_oc, "na": na, "team_active": "active"}
	raise Http404("Does not exist")
	return render(request, template_name, context)

