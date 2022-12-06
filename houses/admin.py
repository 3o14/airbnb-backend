from django.contrib import admin
from .models import House

# Register your models here.

# admin패널에 'House'라는 model을 등록하고 싶다는 의미
@admin.register(House) # decorator 이 데코레이터의 의미: 이 class가 House model을 통제할 것이다.
class HouseAdmin(admin.ModelAdmin):
    pass # 상속받고 아무것도 수정하지 않을 경우

# class를 만듬. 이 class는 ModelAdmin(어드민패널)의 모든 것을 상속받음