from django.db import models
from django.utils.html import mark_safe
class Image(models.Model):
	img = models.ImageField(upload_to='gallery_items/', blank=True, null=True)
	formal_caption = models.CharField(max_length=500,default='caption')
	informal_caption = models.CharField(max_length=500,default='caption')
	serial_number = models.FloatField(default=1)
	
	class Meta:
		ordering = ["serial_number"]
        
	def __str__(self):
			return str(self.img)+' - '+str(self.serial_number)

	def formal(self):
		if(self.formal_caption!='caption'):
			return self.formal_caption
		else:
			return self.informal_caption
	def informal(self):
		if(self.informal_caption!='caption'):
			return self.informal_caption
		else:
			return self.informal_caption

	def image_tag(self):
            return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.img))		
