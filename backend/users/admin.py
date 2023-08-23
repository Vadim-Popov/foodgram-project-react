from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

admin.site.unregister(User)  # Удалить регистрацию модели User


class CustomUserAdmin(UserAdmin):
    list_display = (
        'id', 'username', 'email',
        'first_name', 'last_name', 'date_joined',)
    search_fields = ('email', 'username')
    list_filter = ('date_joined', 'email', 'username')
    empty_value_display = '-пусто-'


admin.site.register(User, CustomUserAdmin)
