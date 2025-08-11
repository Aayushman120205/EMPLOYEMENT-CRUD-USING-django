from django.contrib import admin
from .models import Employee, Department

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'Email', 'Contact', 'Date_of_Joining','Password',)
    list_filter = ('Date_of_Joining','Last_Name',)
    search_fields = ('First_Name','Contact','Email')
    ordering = ('Date_of_Joining',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display  = ('Emp_Name','Dep_Name')

admin.site.register(Employee, EmployeeAdmin)

admin.site.register(Department, DepartmentAdmin)

