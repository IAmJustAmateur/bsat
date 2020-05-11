from django.contrib import admin

from . models import (Cleaning, Team, Driver, Add_work)
# Register your models here.

admin.site.register(Cleaning)
admin.site.register(Team)
admin.site.register(Driver)
admin.site.register(Add_work)
