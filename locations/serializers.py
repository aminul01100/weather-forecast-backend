from rest_framework import serializers
from django.utils import timezone

from .models import District

from services.open_meteo_service import get_temperature_list, get_daily_temperature


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"


class IsDestinationColderSerializer(serializers.Serializer):
    current_lat = serializers.DecimalField(max_digits=22, decimal_places=16, write_only=True, required=True)
    current_long = serializers.DecimalField(max_digits=22, decimal_places=16, write_only=True, required=True)
    destination_lat = serializers.DecimalField(max_digits=22, decimal_places=16, write_only=True, required=True)
    destination_long = serializers.DecimalField(max_digits=22, decimal_places=16, write_only=True, required=True)
    travel_date = serializers.DateField(write_only=True, required=True)

    is_destination_colder = serializers.SerializerMethodField(read_only=True)

    class Meta:
        fields = ['is_destination_colder']

    def get_is_destination_colder(self, obj):
        def get_param(lat, long):
            params = {
                "latitude": lat,
                "longitude": long,
                "daily": ["temperature_2m_max"],
                "start_date": self.validated_data.get("travel_date").strftime('%Y-%m-%d'),
                "end_date": self.validated_data.get("travel_date").strftime('%Y-%m-%d')
            }
            return params

        current_temperature = get_daily_temperature(get_param(self.validated_data.get("current_lat"), self.validated_data.get("current_long")))
        destination_temperature = get_daily_temperature(get_param(self.validated_data.get("destination_lat"), self.validated_data.get("destination_long")))

        return destination_temperature < current_temperature

    def validate(self, attrs):
        value = attrs.get('travel_date')
        max_days_difference = 16

        # Get the current date
        today = timezone.now().date()

        # Calculate the difference in days
        days_difference = (value - today).days

        # Check if the travel_date is within the allowed range
        if days_difference > max_days_difference:
            raise serializers.ValidationError("Travel date cannot be more than 16 days from today.")

        return attrs
