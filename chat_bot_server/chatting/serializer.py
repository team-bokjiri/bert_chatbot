from rest_framework import serializers

from .models import *


class MyChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChat
        exclude = ['user']
