from django.contrib import admin
from .models import Wishlists

@admin.register(Wishlists)
class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "created_at",
        "updated_at",
    )