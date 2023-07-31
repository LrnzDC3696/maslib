from rest_framework import serializers
from base.models import Show, UserShowList


class UserShowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserShowList
        fields = "__all__"


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = "__all__"
