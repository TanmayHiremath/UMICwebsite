from django.contrib import admin
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

class PropertyImageInline1(admin.TabularInline):
    model = OC
    extra = 2

class PropertyImageInline2(admin.TabularInline):
    model = TeamMember
    extra = 3

class PropertyImageInline3(admin.TabularInline):
    model = StudentAdvisor
    extra = 3

class PropertyImageInline4(admin.TabularInline):
    model = Faculty
    extra = 1

class PropertyAdmin1(admin.ModelAdmin):
    inlines = [ PropertyImageInline1, PropertyImageInline2, PropertyImageInline3, PropertyImageInline4]

admin.site.register(CurrentTeam, PropertyAdmin1)

class PropertyImageInline21(admin.TabularInline):
    model = PastOC
    extra = 2

class PropertyImageInline22(admin.TabularInline):
    model = NotableAlumni
    extra = 3

class PropertyAdmin2(admin.ModelAdmin):
    inlines = [ PropertyImageInline21, PropertyImageInline22]

admin.site.register(PastTeam, PropertyAdmin2)
# Register your models here.
