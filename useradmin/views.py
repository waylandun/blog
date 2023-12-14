from django.shortcuts import render,HttpResponse
from .models import UserModel

# Create your views here.
def index(request):
    # 增 insert
    # UserModel.objects.create(username='zhangsan', email='you33@qq.com', password='1233ee')

    # 删 del
    # UserModel.objects.filter(id=7).delete()

    # 改 update
    # UserModel.objects.filter(id=6).update(username='lol')

    # 查 select
    # result = UserModel.objects.filter(id=1)
    # result = UserModel.objects.filter(id=1).first()  # first() 查询到的第一个
    # print(result)  # QuerySet 集合
    # print(result[0].username)
    return render(request, 'login_register.html')

def login(request):
    if request.method == 'POST':
        print('login')
        print(request.POST.get('username'))
        print(request.POST.get('password'))
    return render(request, 'login_register.html')

def register(request):
    if request.method == 'POST':
        print('register')
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        print(request.POST.get('email'))
        print(request.POST.get('repassword'))
    return render(request, 'login_register.html')

def forgot(request):
    return HttpResponse("forgot")