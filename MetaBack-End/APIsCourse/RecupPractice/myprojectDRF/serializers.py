from rest_framework import serializers
from .models import SuperModel
from rest_framework.validators import ValidationError
import bleach
class SuperModelSerializer(serializers.ModelSerializer):
     def validate_numberOfWorkers(self, value):
          if (value < 0):
           raise serializers.ValidationError('Workers cannot be negative')
          
    # def validate(self, attrs):
     #     attrs['meat'] = bleach.clean(attrs['meat'])
      #    if(attrs['workers']<0):
       #        raise (ValidationError("WTF you can't do that "))
        #  return super().validate(attrs)
     
     numberOfWorkers = serializers.IntegerField(source = 'workers')
     class Meta:
          model = SuperModel
          fields = ['id','vegtables','meat','numberOfWorkers']
          extra_kwargs = {'workers':{'min_value':0}}