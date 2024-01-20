from django.contrib import admin
from .models import Todo

# admin.site.register(Todo)

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['todo',]
    list_filter=[''created_at,"updated_at"]