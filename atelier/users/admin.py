from django.contrib import admin

# Register your models here.
from .models import Person
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
        search_fields=('first_name','last_name')
admin.site.register(Person,PersonAdmin)