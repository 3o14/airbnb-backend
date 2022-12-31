from django.db import models
from common.models import CommonModel

class ChattingRoom(CommonModel):
    
    """ Room Model Definition """
    
    user = models.ManyToManyField(
        "users.User",
        related_name="chatting_rooms",
    )
    
    def __str__(self) -> str:
        return "Catting Room."
    
class Message(CommonModel):
    
    """ Message Model Definition """
    
    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="messages",
        
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )
    
    def __str__(self):
        return f"{self.user} says : {self.text}"