from django.db import models

class Project(models.Model):
	image = models.ImageField(upload_to='models/', blank=True, null=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	content = models.TextField(null=True, blank=True)
	no_image = models.IntegerField(null=False, blank=False, default=0)
	class Meta:
		ordering = ['no_image', '-id']
	def __str__(self):
		return self.name
# Create your models here.
