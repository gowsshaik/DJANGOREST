from django.db.models import fields
from .models import Details
from rest_framework import serializers

class DetailSer(serializers.ModelSerializer):
    class Meta:
        model=Details
        fields=['name','location','city']

        
