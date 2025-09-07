from django.contrib import admin
from .models.area import Area
from api.models.house import House
from api.models.review import Review
from api.models.favorite import Favorite

admin.site.register( Area)   
admin.site.register(House)  
admin.site.register(Review) 
admin.site.register(Favorite)                        