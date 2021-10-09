from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer

from .models import Employee
from .serializers import EmployeeSerializer


def employee_list(request):
    """
    simplest list django function based view that returns json data
    """
    emp = Employee.objects.all()
    # < QuerySet[ < Employee: Employee object(1) >] >
    serializer = EmployeeSerializer(emp, many=True)
    # serializer.data : [OrderedDict([('name', 'Rinkesh'), ('employee_code', 1), ('department', 'Developer')]),
    #                     OrderedDict([('name', 'Nikunj'), ('employee_code', 2), ('department', 'Developer')])]

    # if using HttpResponse use this code
    # json_data = JSONRenderer().render(serializer.data)
    # # b'[{"name":"Rinkesh","employee_code":1,"department":"Developer"}]'
    # return HttpResponse(json_data, content_type="application/json")

    # if using JsonResponse use this code
    return JsonResponse(serializer.data, safe=False)     # paas safe=False so it can return non dict data


def employee_detail(request, pk):
    """
    simplest detail django function based view that returns json data
    """
    emp = Employee.objects.get(id=pk)
    # Employee object(1)
    serializer = EmployeeSerializer(emp)
    # serializer.data : {'name': 'Rinkesh', 'employee_code': 1, 'department': 'Developer'}

    # if using HttpResponse use this code
    # json_data = JSONRenderer().render(serializer.data)
    # b'{"name":"Rinkesh","employee_code":1,"department":"Developer"}'
    # return HttpResponse(json_data, content_type="application/json")

    # if using JsonResponse use this code
    return JsonResponse(serializer.data)
