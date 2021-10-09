from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    employee_code = serializers.IntegerField()
    department = serializers.CharField(max_length=50)
