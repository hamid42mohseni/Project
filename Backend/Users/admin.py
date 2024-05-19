from .models import User
from django.contrib import admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("password", "username")
    list_display = ("username", "phone_number",
                    "is_staff", "is_active", "last_login")
    fields = ("username", "phone_number", "password", "is_staff", "is_active")
