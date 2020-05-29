from django.urls import path
from .views import home, AddVehicle, ShowVehicleList, ShowVehicleDetail, UpdateVehicle, create_profile, \
    ShowUserProfile, register
urlpatterns = [
    path('', home, name="home"),
    path('vehicle/list', ShowVehicleList, name="vehicle-list-view"),
    path('vehicle/detail/<int:pk>', ShowVehicleDetail, name="vehicle-detail-view"),
    path('vehicle/update/<int:pk>', UpdateVehicle, name="vehicle-update-view"),
    path('vehicle/add/', AddVehicle, name="vehicle-add-view"),
    path('upload/',create_profile, name='upload'),
    path('profile/', ShowUserProfile, name='profile'),
    path('register/', register, name='register'),
]