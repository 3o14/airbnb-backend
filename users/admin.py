from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # 사용자 관리하기에서 수정할 수 있는 내용들
    fieldsets = (
        (
            "Profile", 
            {
                "fields": ("username", "password", "name", "email", "is_host"),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",), # 접기
            },
        ),
        (
            "Important dates", 
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",), # 접기
            }
        )
    )
    
    # 사용자 리스트에서 보이게 할 컬럼 설정
    list_display = ("username", "email", "name", "is_host")