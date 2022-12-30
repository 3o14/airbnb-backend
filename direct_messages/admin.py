from django.contrib import admin
from .models import Message, ChattingRoom

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    
    list_display = (
        "user",
        "text",
        "room",
        "created_at"
    )

    list_filter = (
        "created_at",
    )
    
@admin.register(ChattingRoom)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "created_at",
        "updated_at",
    )
    
    list_filter = (
        "created_at",
    )