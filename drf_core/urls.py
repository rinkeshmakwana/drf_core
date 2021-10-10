from django.contrib import admin
from django.urls import path

from api.views import employee_list, employee_detail, employee_create, employee_api, EmployeeAPI

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('api/employees/', employee_list),
    # path('api/employee/<int:pk>/', employee_detail),
    # path('api/employee/create/', employee_create),

    # all above 3 list, create, retrieve, update functionality in single api
    # path('api/', employee_api),
    path('api/', EmployeeAPI.as_view()),
]
