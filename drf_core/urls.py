from django.contrib import admin
from django.urls import path

from api.views import employee_list, employee_detail, employee_create, employee_api, EmployeeAPI, employee_api_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('api/employees/', employee_list),
    # path('api/employee/<int:pk>/', employee_detail),
    # path('api/employee/create/', employee_create),

    # all above 3 list, create, retrieve, update functionality in single api
    # path('api/', employee_api),           # function based
    # path('api/', EmployeeAPI.as_view()),  # class based

    path('api/', employee_api_view),
    path('api/<int:pk>/', employee_api_view),
]
