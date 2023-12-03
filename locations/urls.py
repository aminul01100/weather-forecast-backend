from django.urls import path

from .views import ListDistricts, GetTravelDecision

app_name = 'locations'

urlpatterns = [
    path('district-list', ListDistricts.as_view(), name='coldest-district-list'),
    path('travel-decision', GetTravelDecision.as_view()),
]
