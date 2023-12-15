from django.shortcuts import render, HttpResponse

from .models import Department, UserInfo


# Create your views here. 20221214
def employee(request):
    return render(request,'employee.html')


def department(request):
    departs = Department.objects.all()
    meta = {}
    meta["departs"] = departs
    return render(request, 'department.html', meta)
