from django.shortcuts import render, HttpResponse, redirect

from .models import Department, UserInfo


# Create your views here. 20221214
def employee_list(request):
    return render(request, 'employee.html')


def department_list(request):
    departs = Department.objects.all()
    meta = {}
    meta["departs"] = departs
    return render(request, 'department.html', meta)


def add_department(request):
    if request.POST:
        title = request.POST.get('title', "")
        dh = request.POST.get('dh', '')
        Department.objects.create(title=title, dh=dh)
        return redirect(to="department_list")
    return render(request, 'add_depart.html')


def update_department(request, depart_id):
    # depart_id = request.GET.get('id', '')
    print()
    depart = Department.objects.filter(id=int(depart_id)).first()
    if request.POST:
        title = request.POST.get('title', "")
        dh = request.POST.get('dh', '')
        Department.objects.filter(id=depart_id).update(title=title, dh=dh)
        return redirect(to="department_list")
    return render(request, 'update_depart.html', {'depart': depart})
