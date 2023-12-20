from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employee_list),
    path('depart/list/', views.department_list, name="department_list"),
    path('depart/add/', views.add_department, name="add_department"),
    path('depart/update/<int:depart_id>/', views.update_department, name="update_department"),
]
