from django.shortcuts import render, redirect
from django import forms

from .models import Department, UserInfo


# Create your views here. 20221214
def department_list(request):
    '''
    部门列表
    :param request:
    :return:
    '''
    # 过滤掉已删除的数据
    departs = Department.objects.filter(is_delete=False)
    meta = {}
    meta["departs"] = departs
    meta["dep_active"] = "active"
    return render(request, 'department.html', meta)


def add_department(request):
    '''
    添加新部门
    :param request:
    :return:
    '''
    if request.POST:
        title = request.POST.get('title', "")
        dh = request.POST.get('dh', '')
        Department.objects.create(title=title, dh=dh)
        return redirect(to="department_list")
    return render(request, 'add_depart.html')


def update_department(request, depart_id):
    depart = Department.objects.filter(id=depart_id).first()
    if request.POST:
        title = request.POST.get('title', "")
        dh = request.POST.get('dh', '')
        Department.objects.filter(id=depart_id).update(title=title, dh=dh)
        return redirect(to="department_list")
    return render(request, 'update_depart.html', {'depart': depart})


def delete_department(request, depart_id):
    result = Department.objects.filter(id=depart_id).update(is_delete=True)
    return redirect(to='department_list')


'''
class UserFrom(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.CharField(widget=forms.IntegerField)
    account = forms.CharField(widget=forms.DecimalField)
    create_time = forms.CharField(widget=forms.DateTimeField)
    gender = forms.CharField(widget=forms.ChoiceField)
'''


class UserForm(forms.ModelForm):
    # xx = forms.CharField(widget=forms.CharField)  # 继承的基础上自定义
    class Meta:
        model = UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart']
        # fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart','xx']


def employee_list(request):
    meta = {}
    meta["emp_active"] = "active"
    return render(request, 'employee.html', meta)


def add_employee(request):
    user_form = UserForm()
    return render(request, 'add_employee.html', {'userfroms': user_form})
