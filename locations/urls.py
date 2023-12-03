from django.urls import path

from .views import ListDistricts

app_name = 'locations'

urlpatterns = [
    path('district-list', ListDistricts.as_view(), name='coldest-district-list'),
]
