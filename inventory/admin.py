from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class DesktopAdmin(ImportExportModelAdmin):
    class Meta:
        model=Desktops

class LaptopAdmin(ImportExportModelAdmin):
    class Meta:
        model=Laptops

class MobileAdmin(ImportExportModelAdmin):
    class Meta:
        model=Mobiles

admin.site.register(Desktops,DesktopAdmin)
admin.site.register(Laptops,LaptopAdmin)
admin.site.register(Mobiles,MobileAdmin)