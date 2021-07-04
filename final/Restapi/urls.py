from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Restapi import views
    


urlpatterns = [
        path('data/<str: state>/<city>/', views.StateCity.as_view()),

    path('data/', views.HospitalsListbystate.as_view()),
    path('data/<str:state>/', views.HospitalsListbystate.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)
