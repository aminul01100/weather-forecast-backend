from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import District
from .serializers import DistrictSerializer, IsDestinationColderSerializer


class ListDistricts(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = District.objects.all().order_by('average_temperature')
    serializer_class = DistrictSerializer


class GetTravelDecision(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            serializer = IsDestinationColderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
