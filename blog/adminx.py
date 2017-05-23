import xadmin

from .models import PersonalInfo
# Register your models here.
class PersonalInfoAdmin(object):
    list_display = ['name', 'sex']
    list_filter = ['name', 'sex']
xadmin.site.register(PersonalInfo,PersonalInfoAdmin)