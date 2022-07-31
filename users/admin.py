from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)  # decorator
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "N분의1",
            {
                "fields": (
                    "프로필",
                    "성별",
                    "최애메뉴",
                    "생일",
                    "착한사용자",
                )
            },
        ),
    )
