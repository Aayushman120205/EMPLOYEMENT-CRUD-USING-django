from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import Http404

# GET all employees
class EmployeeListView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

# POST: Create new employee
class EmployeeCreateView(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET employee by ID
class EmployeeGetByIdView(APIView):
    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

# DELETE employee by ID
class EmployeeDeleteByIdView(APIView):
    def delete(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
