from django.contrib import admin
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','status') #presne toto sa vypise v tej appke

admin.site.register(Todo,TodoAdmin) #do administracii registruj podla tohto modelu tstranku

#po migracii vytvorime tabulku v databze