from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Employee


# class EmployeeSerializer(serializers.Serializer):
#     """custom serializer"""
#
#     def start_with_r(value):
#         if value[0].lower() != 'r':
#             raise serializers.ValidationError("Name should be start with r")
#
#     name = serializers.CharField(max_length=100, validators=[start_with_r])     # validator as custom function
#     employee_code = serializers.IntegerField()
#     department = serializers.CharField(max_length=50)
#
#     def create(self, validate_data):
#         return Employee.objects.create(**validate_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.employee_code = validated_data.get('employee_code', instance.employee_code)
#         instance.department = validated_data.get('department', instance.department)
#         instance.save()
#         return instance
#
#     # field level validation
#     def validate_employee_code(self, value):
#         if value >= 200:
#             raise serializers.ValidationError("Employees quota over")
#
#     # object level validation
#     def validate(self, data):
#         name = data.get('name')
#         department = data.get('department')
#         if name.lower() == 'rinkesh' and department.lower() != 'developer':
#             raise ValidationError("Department must be developer")
#         return data


class EmployeeSerializer(serializers.ModelSerializer):
    """model serializer"""

    # name = serializers.CharField(read_only=True)        # to make single field read only when update

    def start_with_r(self, value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError("Name should be start with r")
    name = serializers.CharField(validators=[start_with_r])     # validator as custom method

    class Meta:
        model = Employee
        fields = ['id', 'name', 'employee_code', 'department']
        # read_only_fields = ['name', 'employee_code']        # to make multiple field read only when update
        # extra_kwargs = {'name': {'read_only': True}}        # to make single field read only when update

    # field level validation
    def validate_employee_code(self, value):
        if value >= 200:
            raise serializers.ValidationError("Employees quota over")

    # object level validation
    def validate(self, data):
        name = data.get('name')
        department = data.get('department')
        if name.lower() == 'rinkesh' and department.lower() != 'developer':
            raise ValidationError("Department must be developer")
        return data
