from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Message, User

class CurrentUserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="get_full_name", read_only=True)
    gender_display = serializers.CharField(source="get_gender_display", read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "last_login",
            "username",
            "full_name",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "date_joined",
            "gender_display",
            "avatar",
            "about",
            "is_banned"
        )

class UsersSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="get_full_name", read_only=True)
    gender_display = serializers.CharField(source="get_gender_display", read_only=True)
    class Meta:
        model = User
        fields = (
            "id",
            "last_login",
            "username",
            "full_name",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "date_joined",
            "gender_display",
            "avatar",
            "about",
            "is_banned"
        )
        
class MessageSerializer(ModelSerializer):
    usermessage_display = serializers.SerializerMethodField()

    def get_usermessage_display(self, obj):
        if not obj.usermessage:
            return ""
        return obj.usermessage.username

    class Meta:
        model = Message
        fields = [
            "id",
            "usermessage",
            "usermessage_display",
            "textmessage",
            "datemessage",
            "is_private",
            "reactionscount"
        ]
        read_only_fields = ['id', 'usermessage', 'datemessage', 'reactionscount']
    

