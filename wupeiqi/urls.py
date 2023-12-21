from django.urls import path
from . import views

urlpatterns = [
    path('depart/list/', views.department_list, name="department_list"),
    path('depart/add/', views.add_department, name="add_department"),
    path('depart/update/<int:depart_id>/', views.update_department, name="update_department"),
    path('depart/delete/<int:depart_id>/', views.delete_department, name="delete_department"),

    path('employee/list/', views.employee_list, name="employee_list"),
    path('employee/add/', views.add_employee, name="add_employee"),

]
