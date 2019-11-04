from django.contrib import admin
from django.urls import path, include
from car.views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homepage'),
    path('api/car/', include('car.api.urls'))
]
