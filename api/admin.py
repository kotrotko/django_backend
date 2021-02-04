from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'phone_number', 'is_staff', )
    list_filter = ('phone_number', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': (
            'is_superuser',
            'is_staff',
            'date_of_birth',
            'phone_number',
            'password',
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'date_of_birth', 'password1', 'password2', 'is_staff', ),
        }),
    )
    search_fields = ('phone_number', )
    ordering = ('phone_number', 'id', )

admin.site.register(CustomUser, CustomUserAdmin)
