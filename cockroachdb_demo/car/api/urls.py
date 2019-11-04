from django.urls import path
from .views import (
    CarCreateApiView,
    CarListApiView,
    CarDetailApiView,
    CarUpdateApiView,
    CarDeleteApiView
)

urlpatterns = [
    path('create/', CarCreateApiView.as_view(), name='car_create'),
    path('', CarListApiView.as_view(), name='car_list'),
    path('<pk>/', CarDetailApiView.as_view(), name='car_detail'),
    path('<pk>/edit/', CarUpdateApiView.as_view(), name='car_edit'),
    path('<pk>/delete/', CarDeleteApiView.as_view(), name='car_delete')
]
