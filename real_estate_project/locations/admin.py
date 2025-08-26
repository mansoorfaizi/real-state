from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Province, Timestamp, District

admin.site.register(Province)
admin.site.register(Timestamp)
admin.site.register(District)
