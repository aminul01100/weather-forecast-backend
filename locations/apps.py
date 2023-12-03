from django.apps import AppConfig


class LocationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'locations'

    # update the temperatures of the districts each time the server runs, and it's a background task. and this task is
    # set as a scheduled task as well that will run every day at 11am and 11pm
    def ready(self):
        try:
            from locations.tasks import update_district_temperatures
            update_district_temperatures.delay()
        except Exception as e:
            pass
