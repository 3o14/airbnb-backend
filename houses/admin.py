from django.contrib import admin
from .models import House

# Register your models here.

# admin패널에 'House'라는 model을 등록하고 싶다는 의미
@admin.register(House) # decorator 이 데코레이터의 의미: 이 class가 House model을 통제할 것이다.
class HouseAdmin(admin.ModelAdmin):
    
    # column을 보여주는 리스트 (보여 줄 필드를 리스트 안에 넣기) -> 리스트보다 튜플이 더 자주 사용됨
    list_display = (
        "name",
        "price_per_night",
        "address",
        "pets_allowed"
    )
    
    # 필터링 할 메뉴
    list_filter = ("price_per_night", "pets_allowed")
    
# class를 만듬. 이 class는 ModelAdmin(어드민패널)의 모든 것을 상속받음