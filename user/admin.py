from django.contrib import admin
from .models import User


def activate_user(modeladmin, request, queryset):
    rows_updated = queryset.update(is_active=True)
    if rows_updated == 1:
        subject = 'user'
    else:
        subject = 'users'
    modeladmin.message_user(request, '{} {} get activated'.format(rows_updated, subject))
activate_user.short_description = 'Activate selected users'


def deactivate_user(modeladmin, request, queryset):
    rows_updated = queryset.update(is_active=False)
    if rows_updated == 1:
        subject = 'user'
    else:
        subject = 'users'
    modeladmin.message_user(request, '{} {} get deactivated'.format(rows_updated, subject))
deactivate_user.short_description = 'Deactivate selected users'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name_user', 'last_name_user', 'email_user', 'is_active')
    search_fields = ['user', 'first_name_user', 'last_name_user', 'email_user',]
    actions = [activate_user, deactivate_user, ]

    def first_name_user(self, obj):
        if obj.user:
            return obj.user.first_name
        else:
            return None
    first_name_user.short_description = 'first name'

    def last_name_user(self, obj):
        if obj.user:
            return obj.user.last_name
        else:
            return None
    last_name_user.short_description = 'last name'
    
    def email_user(self, obj):
        if obj.user:
            return obj.user.email
        else:
            return None
    email_user.short_description = 'email'


from django.contrib.admin.models import LogEntry
LogEntry.objects.all().delete()
