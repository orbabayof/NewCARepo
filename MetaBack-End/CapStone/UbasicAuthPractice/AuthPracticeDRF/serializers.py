from rest_framework import serializers
from . import models

class MenuSerializers(serializers.ModelSerializer):
     class Meta:
          model = models.Menu
          fields = "__all__"