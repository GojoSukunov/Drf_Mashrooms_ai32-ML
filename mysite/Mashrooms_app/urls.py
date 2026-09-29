from django.urls import path
from .views import MashroomsPredictionViewSet

urlpatterns=[
    path('mashrooms_prediction',MashroomsPredictionViewSet.as_view(),name='mashrooms-prediction')
]