from django.contrib import admin

from . models import (Cleaning, Team, Driver, Add_work, Car_Num, Car_Type, Trail_Type, Tank_Num)
# Register your models here.

admin.site.register(Cleaning)
admin.site.register(Team)
admin.site.register(Driver)
admin.site.register(Add_work)
admin.site.register(Car_Num)
admin.site.register(Car_Type)
admin.site.register(Trail_Type)
admin.site.register(Tank_Num)

