from django.contrib import admin
from django.urls import path

from api.views import employee_list, employee_detail, employee_create, employee_api, EmployeeAPI, employee_api_view, \
    EmployeeAPIView, EmployeeListView, EmployeeCreateView, EmployeeRetrieveView, EmployeeUpdateView, EmployeeDeleteView, \
    EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('api/employees/', employee_list),
    # path('api/employee/<int:pk>/', employee_detail),
    # path('api/employee/create/', employee_create),

    # all above 3 list, create, retrieve, update functionality in single api
    # path('api/', employee_api),           # function based
    # path('api/', EmployeeAPI.as_view()),  # class based

    # path('api/', employee_api_view),            # function based api list, create view
    # path('api/<int:pk>/', employee_api_view),   # function based api detail, update, delete view
    # path('api/', EmployeeAPIView.as_view()),    # class based api list, create view
    # path('api/<int:pk>/', EmployeeAPIView.as_view()),   # class based api detail, update, delete view

    # path('api/employees/', EmployeeListView.as_view()),
    # path('api/employees/', EmployeeCreateView.as_view()),
    # path('api/employees/<int:pk>/', EmployeeRetrieveView.as_view()),
    # path('api/employees/<int:pk>/', EmployeeUpdateView.as_view()),
    # path('api/employees/<int:pk>/', EmployeeDeleteView.as_view()),

    # put all above 5 api view functionality in 2 views only
    path('api/employees/', EmployeeListCreateView.as_view()),
    path('api/employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view()),

]
