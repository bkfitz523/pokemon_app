from django.contrib import admin
from collection.models import Region, Type

# Register your models here.


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)
admin.site.register(Region, RegionAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)
admin.site.register(Type, TypeAdmin)