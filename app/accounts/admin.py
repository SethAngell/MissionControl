from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "name",
        "phone_number",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "name",
        "phone_number",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("phone_number", "password", "name")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                    "name",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("phone_number",)
    ordering = ("phone_number",)


admin.site.register(CustomUser, CustomUserAdmin)
