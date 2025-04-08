from django.contrib import admin
from .models import AdminLog
from .models import CustomUser
from django.contrib.auth import get_user_model

# Register your models here.
@admin.register(AdminLog)
class AdminLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp', 'details')
    list_filter = ('action', 'timestamp')
    search_fields = ('user__username', 'details')


CustomUser = get_user_model()  # Get the actual user model

admin.site.register(CustomUser)  
 