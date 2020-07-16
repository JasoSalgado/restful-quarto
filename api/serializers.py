"""
ModelSerializer is used to serialize Django Models.
HyperlinkedModelSerializer provides the same functionalitty as the aforementioned, but instead of the primary key, it displays a hyperlink to the model instance in the "url" field
"""
from rest_framework import serializers
from api.models import User, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required = True)
    
    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}
    
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user = user, **profile_data)
        return user


    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        
        profile.location = profile_data.get('location', profile.location)
        profile.description = profile_data.get('description', profile.description)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.active = profile_data.get('active', profile.active)
        profile.picture = profile_data.get('picture', profile.picture)
        profile.save()
        
        return instance
        
        
        