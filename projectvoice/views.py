from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.


class VoiceRecordingViewSet(viewsets.ModelViewSet):
    queryset = Recordings.objects.all()
    serializer_class = VoiceRecordingSerializer
    