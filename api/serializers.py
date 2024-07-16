from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import *


class ProfileSerializer(serializers.ModelSerializer):

    def create(self,user, **validated_data,):
        if Profile.objects.filter(user=user).exists():
            profile = Profile.objects.get(user=user)
            profile.phone_number = validated_data['phone_number']
            profile.profile_pic = validated_data['profile_pic']
            profile.Name = validated_data['Name']
            profile.save()
            return profile
        profile = Profile.objects.create(**validated_data, user=user,)
        return profile

    class Meta:
        model = Profile
        fields = (
            'phone_number',
            'profile_pic',
            'Name',
        )

class DeviceSerializer(serializers.ModelSerializer):

    def create(self, user, **validated_data):
        owner = Profile.objects.get(user=user)
        device = Device.objects.create(**validated_data, user=user, owner=owner)
        return device
    class Meta:
        model = Device
        fields = (
            'name',
            'type',
        )