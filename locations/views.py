from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import District
from .serializers import DistrictSerializer


class ListDistricts(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = District.objects.all().order_by('average_temperature')
    serializer_class = DistrictSerializer

# Create your views here.
