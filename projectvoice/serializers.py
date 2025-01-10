from rest_framework import serializers
from .models import *

class VoiceRecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recordings
        fields = '__all__'
