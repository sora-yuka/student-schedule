from typing import Dict, Any
from django.utils import timezone
from rest_framework import serializers

from .models import Room, Message


class RoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Room
        fields = "__all__"
        
        
class MessageSerializer(serializers.ModelSerializer):
    current_user = serializers.SerializerMethodField("_user")
    
    def _user(self, obj: Message):
        request = self.context.get("request", None)
        
        if request:
            return request.user.email
    
    class Meta:
        model = Message
        exclude = ["timestamp", "room"]
    
    def to_representation(self, instance: Message) -> Dict[str, Any]:
        representation = super().to_representation(instance=instance)
        local_timestamp = timezone.localtime(instance.timestamp)
        
        representation.update({
            "id": instance.id,
            "date": local_timestamp.strftime("%d.%m.%Y"),
            "time": local_timestamp.strftime("%H:%M"),
            "sender": instance.sender.email,
            "receiver": instance.receiver.email,
            "room": instance.room.room,
        })
        
        return representation