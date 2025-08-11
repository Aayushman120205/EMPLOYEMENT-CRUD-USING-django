from django.urls import  path
from .views import EmployeeCreateView,EmployeeListView,EmployeeDeleteByIdView,EmployeeGetByIdView

urlpatterns = [
    path('getall-employees/', EmployeeListView.as_view(), name='get-all-employees'),
    path('create-employees/', EmployeeCreateView.as_view(), name='create-employee'),
    path('get-employees/<int:pk>/', EmployeeGetByIdView.as_view(), name='get-employee-by-id'),
    path('delete-employees/<int:pk>/', EmployeeDeleteByIdView.as_view(), name='delete-employee-by-id'),
]