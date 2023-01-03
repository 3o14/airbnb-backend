from django.contrib import admin
from .models import Room, Amenity

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )

    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )
    
    # 방법2 admin.py에 작성
    def total_amenities(self, room):
        print(room)
        return room.amenities.count()

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    
    list_display = (
            "name",
            "description",
            "created_at",
            "updated_at",
        )
    
    readonly_fields = (
        "created_at",
        "updated_at",
    )