from celery import shared_task
from .models import District

from services.open_meteo_service import get_temperature_list


@shared_task
def update_district_temperatures():
    districts = District.objects.all()

    for district in districts:
        try:
            params = {
                "latitude": district.lat,
                "longitude": district.long,
                "hourly": "temperature_2m"
            }
            temperature_list = get_temperature_list(params)

            days = len(temperature_list) // 24

            if days == 0:
                continue

            sum_temp = 0
            for i in range(0, days):
                current_day = i * 24 + 14  # getting current day's 2pm hour
                sum_temp += temperature_list[current_day]

            district.average_temperature = sum_temp / days
            district.save()
        except Exception as e:
            print(f"an error occurred while updated temperature of a district. error: {e}")