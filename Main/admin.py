from django.contrib import admin

from django.contrib.auth.models import Group
# Register your models here.
from Main.models import Heater


class HeaterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Heater, HeaterAdmin)
admin.site.unregister(Group)