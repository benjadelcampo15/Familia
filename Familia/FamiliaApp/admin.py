from django.contrib import admin

from FamiliaApp.models import familiar

class familiarAdmin(admin.ModelAdmin):

    list_display = ('nombre' , 'edad' , 'nacimiento')

admin.site.register(familiar, familiarAdmin)






