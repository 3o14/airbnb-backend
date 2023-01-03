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
    
    search_fields = (
        "name",
        "^price",
        # ^ : ~로 시작하는 방 검색하기
        # = : 완전히 동일한 검색결과 찾기
        # 아무것도 적지 않을 경우 : contains 포함하는 것 검색
        "owner__username"
        # 이렇게도 가능함
    )

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