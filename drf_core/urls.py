from django.contrib import admin
from django.urls import path

from api.views import employee_list, employee_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees/', employee_list),
    path('api/employee/<int:pk>/', employee_detail),
]
