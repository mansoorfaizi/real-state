from django.contrib import admin
from .models.area import Area
from api.models.house import House
from api.models.review import Review

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "district", "timestamp")   
    search_fields = ("name",)   
admin.site.register(House)  
admin.site.register(Review)                          