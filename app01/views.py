from django.shortcuts import render, redirect, HttpResponse
from . import functions


# Create your views here.
# 真正的登录在home函数中
def login(request):
    if request.session.get('is_login', None):  # 将登录信息保存到session中实现重复调用
        return redirect('/home/')
    return render(request, 'login.html', {'error': False})  # 将error参数返回


# 登出
def logout(request):
    if request.session.get('is_login', None):
        request.session.flush()
        return redirect('/login/')


# 注册过渡函数，用于界面跳转
def register(request):
    if request.session.get('is_login', None):
        return redirect('/home/')
    return render(request, 'register.html')


# 注册确认函数
def register_confirm(request):
    if request.method == 'POST':  # 接收到post请求
        name = request.POST.get('name')  # 获得参数并保留到变量
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')  # html标签传递的数据
        types = request.POST.get('types')
        user = functions.find_user(name)  # user获取包含目标name的元组
        if user:  # 如果已经找到user，证明用户名重复，返回error类型为0
            return render(request, 'register.html', {'error': 0})
        if password1 != password2:
            return render(request, 'register.html', {'error': 1})
        if types != '医生' and types != '护士长' and types != '病房护士' and types != '急诊护士':
            return render(request, 'register.html', {'error': 3})
        if functions.add_user(name, password1, types):
            return redirect('/login/')
        else:  # 若上述函数没有成功执行
            return render(request, 'register.html', {'error': 2})


# 主页面交互函数
def home(request):
    if request.session.get('is_login', None):  # 检查登陆状态并传递参数cur为0
        return render(request, 'home.html', {'cur': 0})
    # 登录函数
    if request.method == 'POST':  # 如果抓取到post请求
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = functions.find_name_password(name, password)  # 核对密码，该函数返回了一个元组列表
        if user:  # 如果user成功获取，即登陆成功，将信息保存到session中
            request.session['is_login'] = True
            request.session['name'] = user[0][0]
            request.session['password'] = user[0][1]
            request.session['type'] = user[0][2]
            return render(request, 'home.html', {'cur': 0})
        else:
            return render(request, 'login.html', {'error': True})  # 登陆失败则返回错误标签
    else:  # 没有post请求
        return redirect('/login/')


def patient(request):
    if request.session.get('is_login', None):
        if request.session.get('type') == '医生' or request.session.get('type') == '护士长':
            result = functions.my_patient(request.session.get('name'))
        if request.session.get('type') == '病房护士':
            result = functions.my_patient_ward_nurse(request.session.get('name'))
        patients, idx = [], 1
        for i in result:
            data = {'idx': idx, 'id': i[0], 'age': i[1],
                    'gender': '男' if i[2] else '女', 'level': i[3],
                    'name': i[4], 'section': i[5],
                    'status': i[6], 'ward_name': i[7], 'ward_nurse': i[8]}
            patients.append(data)
            idx += 1
        return render(request, 'patient.html', {'patients': patients, 'cur': 2})  # 返回workers，cur游标返回1
    else:
        return redirect('/login/')


def patient_query(request):
    if request.method == 'POST':
        attribute = request.POST.get('attribute')
        patients, result = [], []
        result = functions.find_patient(attribute)
        idx = 1
        for i in result:
            data = {'idx': idx, 'id': i[0], 'age': i[1],
                    'gender': '男' if i[2] else '女', 'level': i[3],
                    'name': i[4], 'section': i[5],
                    'status': i[6], 'ward_name': i[7], 'ward_nurse': i[8]}
            patients.append(data)
            idx += 1
        return render(request, 'patient.html', {'patients': patients, 'cur': 2})


def patient_information(request, name):
    if request.session.get('is_login', None):
        result = functions.patient_history(name)
        informations, idx = [], 1
        for i in result:
            data = {'idx': idx, 'id': i[0], 'name': i[2],
                    'date': i[1],
                    'temperature': i[3], 'positive': i[4]}
            informations.append(data)
            idx += 1
        return render(request, 'patient_information.html', {'informations': informations})
    else:
        return redirect('/login/')


def nurses(request):
    if request.session.get('is_login', None):
        result = functions.section_nurses(request.session.get('name'))
        nurses, idx = [], 1
        for i in result:
            data = {'idx': idx, 'name': i[0], 'gender': i[1],
                    'type': i[2]}
            nurses.append(data)
            idx += 1
        return render(request, 'nurses.html', {'nurses': nurses, 'cur': 3})
    else:
        return redirect('/login/')


def information(request):
    if request.session.get('is_login', None):
        result = functions.show_information(request.session.get('name'))
        informations, idx = [], 1
        for i in result:
            data = {'idx': idx, 'name': i[0], 'age': i[1],
                    'gender': i[2], 'type': i[3], 'section': i[4]}
            informations.append(data)
            idx += 1
        return render(request, 'information.html', {'informations': informations, 'cur': 1})
    else:
        return redirect('/login/')


def modify_information(request):
    if request.session.get('is_login', None):
        return render(request, 'information_modify.html', {'cur': 1})
    else:
        return redirect('/login/')


def modify_information_confirm(request):
    if request.method == 'POST':  # 接收到post请求
        name = request.POST.get('name')
        age = request.POST.get('age')  # 获得参数并保留到变量
        gender = request.POST.get('gender')
        section = request.POST.get('section')  # html标签传递的数据
        if section != '轻症区域' and section != '重症区域' and section != '危重症区域':  # 如果已经找到user，证明用户名重复，返回error类型为0
            return render(request, 'information_modify.html', {'error': 0, 'cur': 1})
        if gender != '男' and gender != '女':
            return render(request, 'information_modify.html', {'error': 1, 'cur': 1})
        if functions.modify_information(request.session.get('name'), name, age, gender, section):
            return redirect('/information/')
        else:  # 若上述函数没有成功执行
            return render(request, 'information_modify.html', {'error': 2, 'cur': 1})


def report(request):
    if request.session.get('is_login', None):
        return render(request, 'report.html', {'cur': 4})
    else:
        return redirect('/login/')


def report_confirm(request):
    if request.method == 'POST':  # 接收到post请求
        id = request.POST.get('id')  # 获得参数并保留到变量
        name = request.POST.get('name')
        positive = request.POST.get('positive')  # html标签传递的数据
        user = functions.find_patient(name)
        if not user:
            return render(request, 'report.html', {'error': 0, 'cur': 4})
        if request.session.get('type') != '医生':
            return render(request, 'report.html', {'error': 2, 'cur': 4})
        if functions.new_report(id, name, positive):
            return HttpResponse("提交成功!")
        else:  # 若上述函数没有成功执行
            return render(request, 'report.html', {'error': 1, 'cur': 4})


def patient_add(request):
    if request.session.get('is_login', None):
        return render(request, 'patient_add.html', {'cur': 2})
    else:
        return redirect('/login/')


def patient_add_confirm(request):
    if request.method == 'POST':  # 接收到post请求
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')  # html标签传递的数据
        level = request.POST.get('level')  # html标签传递的数据
        section = request.POST.get('section')
        ward_name = request.POST.get('ward_name')
        ward_nurse = request.POST.get('ward_nurse')
        if request.session.get('type') != '急诊护士':
            return render(request, 'patient_add.html', {'error': 0, 'cur': 2})
        if functions.new_patient(name, age, gender, level, section, ward_name, ward_nurse):
            return HttpResponse("提交成功!")
        else:  # 若上述函数没有成功执行
            return render(request, 'patient_add.html', {'error': 1, 'cur': 2})
