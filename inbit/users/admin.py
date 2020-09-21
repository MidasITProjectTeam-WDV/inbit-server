from django.contrib import admin
from users.models import Users

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')