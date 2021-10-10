import io

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Employee
from .serializers import EmployeeSerializer


def employee_list(request):
    """
    simplest list django function based view that returns json data
    """
    emp = Employee.objects.all()
    # < QuerySet[ < Employee: Employee object(1) >] >
    serializer = EmployeeSerializer(emp, many=True)     # model instance into Python native datatype
    # serializer.data : [OrderedDict([('name', 'Rinkesh'), ('employee_code', 1), ('department', 'Developer')]),
    #                     OrderedDict([('name', 'Nikunj'), ('employee_code', 2), ('department', 'Developer')])]

    # if using HttpResponse use this code
    # json_data = JSONRenderer().render(serializer.data)     # serialization : Python native datatype to json data
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
    serializer = EmployeeSerializer(emp)     # model instance into Python native datatype
    # serializer.data : {'name': 'Rinkesh', 'employee_code': 1, 'department': 'Developer'}

    # if using HttpResponse use this code
    # json_data = JSONRenderer().render(serializer.data)     # serialization : Python native datatype to json data
    # b'{"name":"Rinkesh","employee_code":1,"department":"Developer"}'
    # return HttpResponse(json_data, content_type="application/json")

    # if using JsonResponse use this code
    return JsonResponse(serializer.data)


@csrf_exempt
def employee_create(request):
    """
    simplest create django function based view that returns json created data
    """
    if request.method == "POST":
        json_data = request.body
        # b'{"name": "Rahul", "employee_code": "4", "department": "Developer"}'

        # deserialization json data to python native datatype
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        # {'name': 'Rahul', 'employee_code': '4', 'department': 'Developer'}

        serializer = EmployeeSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()           # calls serializer update method if instance exist else create method
            response = {'message': "Data Created"}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def employee_api(request):
    """
    all in one CRUD operation function based view
    """
    if request.method == "GET":
        """list and detail view functionality"""
        json_data = request.body

        # deserialization json data to python native datatype
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id_ = python_data.get('id', None)        # if pass id then it will return instance else return all list
        if id_ is not None:
            emp = Employee.objects.get(id=id_)
            serializer = EmployeeSerializer(emp)     # model instance into Python native datatype
            # serializer.data : {'name': 'Rinkesh', 'employee_code': 1, 'department': 'Developer'}

            # if using HttpResponse use this code
            # json_data = JSONRenderer().render(serializer.data)     # serialization : Python native datatype to json data
            # b'{"name":"Rinkesh","employee_code":1,"department":"Developer"}'
            # return HttpResponse(json_data, content_type="application/json")

            # if using JsonResponse use this code
            return JsonResponse(serializer.data)

        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)     # model instance into Python native datatype
        # serializer.data : [OrderedDict([('name', 'Rinkesh'), ('employee_code', 1), ('department', 'Developer')]),
        #                     OrderedDict([('name', 'Nikunj'), ('employee_code', 2), ('department', 'Developer')])]

        # if using HttpResponse use this code
        # json_data = JSONRenderer().render(serializer.data)     # serialization : Python native datatype to json data
        # b'[{"name":"Rinkesh","employee_code":1,"department":"Developer"}]'
        # return HttpResponse(json_data, content_type="application/json")

        # if using JsonResponse use this code
        return JsonResponse(serializer.data)

    if request.method == "POST":
        """create view functionality"""
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {"msg": "Data Created"}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")

    if request.method == "PUT":
        """update view functionality"""
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id_ = python_data.get('id')
        emp = Employee.objects.get(id=id_)
        serializer = EmployeeSerializer(emp, data=python_data, partial=True)        # pass partial=True for PATCH
        if serializer.is_valid():
            serializer.save()
            response = {"msg": "Partial Data Created"}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")

    if request.method == "DELETE":
        """delete view functionality"""
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id_ = python_data.get('id')
        emp = Employee.objects.get(id=id_)
        emp.delete()
        res = {'msg': "Data Deleted"}
        return JsonResponse(res, safe=False)
