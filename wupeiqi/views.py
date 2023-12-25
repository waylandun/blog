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
    '''
    更新部门信息
    :param request:
    :param depart_id: 部门id
    :return:
    '''
    # post请求为修改后的提交请求
    if request.POST:
        title = request.POST.get('title', "")
        dh = request.POST.get('dh', '')
        Department.objects.filter(id=depart_id).update(title=title, dh=dh)
        return redirect(to="department_list")  # 重定向到部门列表
    # get请求查看对应id的部门信息返回
    depart = Department.objects.filter(id=depart_id).first()
    return render(request, 'update_depart.html', {'depart': depart})


def delete_department(request, depart_id):
    result = Department.objects.filter(id=depart_id).update(is_delete=True)
    return redirect(to='department_list')


'''
# Form 组件渲染前端，方便后端检验用户数据
# 使用过于麻烦，ModelForm可简化部分流程
class UserFrom(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.CharField(widget=forms.IntegerField)
    account = forms.CharField(widget=forms.DecimalField)
    create_time = forms.CharField(widget=forms.DateTimeField)
    gender = forms.CharField(widget=forms.ChoiceField)
'''


class UserForm(forms.ModelForm):
    # xx = forms.CharField(widget=forms.CharField)  # 自定义额外的组件
    class Meta:
        model = UserInfo  # 要渲染的模型
        # 要渲染的模型中的字段 * fields 必填
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart']
        # fields = []  # 不渲染任何组件
        # fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart','xx']


def employee_list(request):
    meta = {}
    meta["emp_active"] = "active"
    return render(request, 'employee.html', meta)


def add_employee(request):
    user_form = UserForm()
    return render(request, 'add_employee.html', {'userfroms': user_form})
