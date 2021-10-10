from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    employee_code = serializers.IntegerField()
    department = serializers.CharField(max_length=50)

    def create(self, validate_data):
        return Employee.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.employee_code = validated_data.get('employee_code', instance.employee_code)
        instance.department = validated_data.get('department', instance.department)
        instance.save()
        return instance
