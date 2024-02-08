from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin



class AccoutAdmin(UserAdmin):
    list_display = ('email','username','date_joined','last_login','is_admin','is_staff','is_superuser')
    search_fields = ('email','username')
    readonly_fields = ('date_joined','last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccoutAdmin)