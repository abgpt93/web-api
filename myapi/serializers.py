from django.db import models
from rest_framework import serializers


from .models import User
#from .models import login
from .models import tweet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name','email','password','password_confirmation')
        '''
        def clean(self):
        cleaned_data=super().clean()     #ensures that any validation logic in parent class is maintained
        valpwd=cleaned_data['password']
        valrpwd=cleaned_data['password_confirmation']

        if valpwd!=valrpwd:
            raise serializers.ValidationError('Password Not matched')'''

class tweetSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = tweet
        fields = ('name','tweet','posted_at')
        read_only_fields = ('posted_at',)
