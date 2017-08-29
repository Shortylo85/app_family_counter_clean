from django.contrib import admin

from ui.models import City, UserCity


class AdminCity(admin.ModelAdmin):
    list_display = ['id','city_name','country', 'lat', 'lng']
    class Meta:    
        model = City
        
class AdminUserCity(admin.ModelAdmin):
    list_display = ['user', 'city']
    class Meta:
        model = UserCity




# Register your models here.
admin.site.register(City, AdminCity)
admin.site.register(UserCity, AdminUserCity)