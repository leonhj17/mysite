from django.contrib import admin

from .models import PersonalInfo
# Register your models here.
class PersonalInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(PersonalInfo,PersonalInfoAdmin)
