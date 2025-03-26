from django.contrib import admin
from myapp.models import UserData

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display=['user_id','name','uploaded_at']
