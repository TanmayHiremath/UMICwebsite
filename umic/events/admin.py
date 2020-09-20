from django.contrib import admin
from .models import Event, Image, Announcement


class PropertyImageInline(admin.TabularInline):
    model = Image
    extra = 3

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline ]

admin.site.register(Event, PropertyAdmin)

admin.site.register(Announcement)
# Register your models here.
