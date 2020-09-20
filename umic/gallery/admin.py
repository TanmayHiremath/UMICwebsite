from django.contrib import admin
from .models import Image



class ImageAdmin(admin.ModelAdmin):

    list_display = ('__str__','formal_caption','informal_caption','image_tag', 'serial_number')
    list_editable = ('formal_caption','informal_caption', 'serial_number')
    list_display_links = ('__str__',)
    ordering = ["serial_number"]

admin.site.register(Image,ImageAdmin)
# Register your models here.
