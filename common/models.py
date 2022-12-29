from django.db import models

class CommonModel(models.Model):
    
    """ Common Model Definition """
    
    # auto_now_add : 이 model이 처음 만들어진 날짜와 시간을 전달
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now : 이 model이 업데이트 될 때마다 그 날짜와 시간을 전달
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
