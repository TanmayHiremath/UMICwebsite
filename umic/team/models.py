from django.db import models

class CurrentTeam(models.Model):
	year = models.IntegerField(null=True, default='2020')
	group_photo = models.ImageField(upload_to='team/', blank=True, null=True)


class OC(models.Model):
    property = models.ForeignKey(CurrentTeam, null=True, related_name='oc', on_delete=models.SET_NULL)
    name = models.CharField(max_length = 50, null=True, blank=False)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to='team/current_team/OC/', blank=True, null=True, default='team/default.png')
    team = models.CharField(max_length = 100, null=True, blank=False)
    subsystem = models.CharField(max_length = 50, null=True, blank=False)
    fb= models.CharField(max_length = 200, null=True, blank=False)
    linkedin = models.CharField(max_length = 200,null=True, blank=False)
    interests = models.TextField(null=True, blank=False)
    yr_dept = models.CharField(max_length=100, null=True, blank=True)

class TeamMember(models.Model):
    property = models.ForeignKey(CurrentTeam, null=True, related_name='member', on_delete=models.SET_NULL)
    name = models.CharField(max_length = 50, null=True, blank=False)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to='team/current_team/team_members/', blank=True, null=True, default='team/default.png')
    team = models.CharField(max_length = 100, null=True, blank=False)
    subsystem = models.CharField(max_length = 100, null=True, blank=False)
    fb= models.CharField(max_length = 200, null=True, blank=False)
    linkedin = models.CharField(max_length = 200, null=True, blank=False)
    interests = models.TextField(null=True, blank=False)
    yr_dept = models.CharField(max_length=100, null=True, blank=False)
    id = models.IntegerField(primary_key=True)

class StudentAdvisor(models.Model):
    property = models.ForeignKey(CurrentTeam, null=True, related_name='advisor', on_delete=models.SET_NULL)
    name = models.CharField(max_length = 50, null=True, blank=False)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to='team/current_team/student_advisors/', blank=True, null=True, default='team/default.png')
    team = models.CharField(max_length = 100, null=True, blank=False)
    subsystem = models.CharField(max_length = 100, null=True, blank=False)
    fb= models.CharField(max_length = 200, null=True, blank=False)
    linkedin = models.CharField(max_length = 200, null=True, blank=False)
    interests = models.TextField(null=True, blank=False)
    yr_dept = models.CharField(max_length=100, null=True, blank=False)
    id = models.IntegerField(primary_key=True)

class Faculty(models.Model):
    property = models.ForeignKey(CurrentTeam, null=True, related_name='faculty', on_delete=models.SET_NULL)
    name = models.CharField(max_length = 50, null=True, blank=False)
    division = models.CharField(max_length = 50, null=True, blank=True, default="UMIC")
    image = models.ImageField(upload_to='team/current_team/faculty/', blank=True, null=True)
    dept = models.CharField(max_length = 100, null=True, blank=True)
    id = models.IntegerField(primary_key=True)


# Past team
class PastTeam(models.Model):
    years = models.CharField(max_length=15, null=True, blank=False, default='2015-2019')

class PastOC(models.Model):
    property = models.ForeignKey(PastTeam, null=True, related_name='past_oc', on_delete=models.SET_NULL)
    name = models.CharField(max_length = 50, null=True, blank=False)
    image = models.ImageField(upload_to='team/past_team/past_oc', blank=True, null=True, default='team/default.png')
    current_company = models.CharField(max_length = 100, null=True, blank=True)

class NotableAlumni(models.Model):
    property = models.ForeignKey(PastTeam, null=True, related_name='notable_alumni', on_delete=models.SET_NULL)
    name = models.CharField(max_length = 50, null=True, blank=False)
    image = models.ImageField(upload_to='team/past_team/notable_alumni', blank=True, null=True, default='team/default.png')
    current_company = models.CharField(max_length = 100, null=True, blank=True)

# Create your models here.
