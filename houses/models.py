from django.db import models

class House(models.Model):
    
    """Model Definition for Houses""" # 모델을 만들때 관례적으로 적는 것(모델에 대한 설명)
    
    name = models.CharField(max_length=140) # 적당한 길이를 가진 문자열
    price = models.PositiveIntegerField # 양의 정수
    description = models.TextField() # 긴 길이를 가진 문자열
    address = models.CharField(max_length=140)