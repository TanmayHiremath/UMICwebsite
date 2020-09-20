from django.db import models

class Event(models.Model):
	title = models.CharField(max_length= 100, null=True, blank=True)
	month_yr = models.CharField(max_length= 100, null=True, blank=True)
	content = models.TextField(null=True, blank=False)
	id = models.IntegerField(null=False, blank=False, primary_key=True)

	class Meta:
		ordering = ['-id']
	def __str__(self):
		return self.title+' - '+self.content[0:30]

class Image(models.Model):
    property = models.ForeignKey(Event, null=True, related_name='event', on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='events/', blank=True, null=True)

class Announcement(models.Model):
	title = models.CharField(max_length= 100, null=True, blank=True)
	month_yr = models.CharField(max_length= 100, null=True, blank=True)
	content = models.TextField(null=True, blank=False)
	link = models.CharField(max_length=300, null=True, blank=True)
	
	class Meta:
		ordering = ['-id']



# Create your models here.
