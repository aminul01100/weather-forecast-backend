from django.apps import AppConfig


class LocationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'locations'

    def ready(self):
        try:
            from locations.tasks import update_district_temperatures
            update_district_temperatures.delay()
        except Exception as e:
            pass
