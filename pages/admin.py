from django.contrib import admin

from .models import *

admin.site.register(Services)
admin.site.register(Service_View)
admin.site.register(Master_and_service_view)
# admin.site.register(Master)
admin.site.register(FeedBack)
# admin.site.register(Applications)
admin.site.register(Records)

admin.site.register(Branch)
admin.site.register(Movement)
# admin.site.register(News)
# admin.site.register(Records)



class Master_Admin(admin.ModelAdmin):
   list_display = ('surname', 'nameofmaster', 'patronymic')

admin.site.register(Master, Master_Admin)


class Salons_Admin(admin.ModelAdmin):
   list_display = ('name',)
   search_fields = ('name',)
admin.site.register (Salons, Salons_Admin)
   
