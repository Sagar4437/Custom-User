from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ['email', 'username', 'last_login', 'is_admin']
    search_fields = ['email', 'username']
    readonly_fields = ['last_login']

    filter_horizontal = []
    list_filter = []
    fieldsets = []


admin.site.register(Account, AccountAdmin) 