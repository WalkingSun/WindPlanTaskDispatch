from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from crons.server.greeter_client import greeter_client
import json
from .models import *
from .common import common
import datetime
from .config import param

def checkUser(request):
    # print(request.session.get('user'))
    if(  request.session.get('user')==None ):
        raise RuntimeError('用户未登录')

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('crons/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'crons/index.html', context)
    # return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'crons/detail.html', {'question': question})

# 用户登录
def login(request):
    result = {}
    try:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if(username==None):
            raise RuntimeError('请输入用户名')
        if(password==None):
            raise RuntimeError('请输入密码')
        psd = common.common.md5(password,'walkingsun')
        # print(psd)
        user = User.objects.filter(username=username,password=psd,isdelete=0).values('id','username')
        if( user.count() == 0 ):
            raise RuntimeError('用户不存在或密码错误')
        user = user[0]
        request.session['user'] = user
        result = {'code': 200, 'msg':user }

    except Exception as e:
        result['code'] = 400
        result['msg'] = str(e)


    return HttpResponse(json.dumps(result), content_type="application/json")

# 添加任务
def add(request):
    result = {}
    try:
        checkUser(request)
        cronsId = request.POST.get("cronsId")
        times = request.POST.get("times")
        command = request.POST.get('command')
        if (cronsId == None):
            raise RuntimeError('请输入cronsId')
        if (times == None):
            raise RuntimeError('请输入times')
        if (command == None):
            raise RuntimeError('请输入command')
        task = Task(comment=cronsId, times=times, command=command, create_userid=request.session.get('user')['id'], create_username=request.session.get('user')['username'],
                    createtime=datetime.datetime.now())
        task.save()
        rpcServer = greeter_client(param._PARAMS['rpcServerHost'],param._PARAMS['rpcServerPort'])
        rpcRes = rpcServer.setPlan(cronsId, times, command)
        result['code']=rpcRes.code
        result['msg']=rpcRes.message
    except Exception as e:
        result['code'] = 400
        result['msg'] = str(e)
        pass
    return HttpResponse(json.dumps(result), content_type="application/json")

# 编辑任务
def edit(request):
    result = {}
    try:
        checkUser(request)
        id = request.POST.get("id")
        cronsId = request.POST.get("cronsId")
        times = request.POST.get("times")
        command = request.POST.get('command')
        if (id == None):
            raise RuntimeError('id缺失')
        if (cronsId == None):
            raise RuntimeError('请输入cronsId')
        if (times == None):
            raise RuntimeError('请输入times')
        if (command == None):
            raise RuntimeError('请输入command')
        Task.objects.filter(id=id,isdelete=0).update(comment=cronsId, times=times, command=command, create_userid=request.session.get('user')['id'])
        rpcServer = greeter_client(param._PARAMS['rpcServerHost'],param._PARAMS['rpcServerPort'])
        rpcRes = rpcServer.updatePlan(cronsId, times, command)
        result['code'] = rpcRes.code
        result['msg'] = rpcRes.message
    except Exception as e:
        result['code'] = 400
        result['msg'] = str(e)
        pass
    return HttpResponse(json.dumps(result), content_type="application/json")

# 删除任务
def delete(request):
    result = {}
    try:
        checkUser(request)
        id = request.POST.get("id")
        cronsId = request.POST.get("cronsId")
        if (id == None):
            raise RuntimeError('id缺失')
        if (cronsId == None):
            raise RuntimeError('请输入cronsId')

        Task.objects.filter(id=id, isdelete=0).update(isdelete=1)
        rpcServer = greeter_client(param._PARAMS['rpcServerHost'], param._PARAMS['rpcServerPort'])
        rpcRes = rpcServer.deletePlan(cronsId)
        result['code'] = rpcRes.code
        result['msg'] = rpcRes.message
    except Exception as e:
        result['code'] = 400
        result['msg'] = str(e)
        pass
    return HttpResponse(json.dumps(result), content_type="application/json")

# 查询系统所有任务
def read(request):
    result = {}
    try:
        checkUser(request)
        host = request.POST.get("host")
        if (host == None):
            host = param._PARAMS['rpcServerHost']

        rpcServer = greeter_client(host, param._PARAMS['rpcServerPort'])
        rpcRes = rpcServer.readPlan()
        result['code'] = rpcRes.code
        result['msg'] = rpcRes.message
    except Exception as e:
        result['code'] = 400
        result['msg'] = str(e)
        pass
    return HttpResponse(json.dumps(result), content_type="application/json")

# 查询host
def host_list(request):
    result = {}
    result['code'] = 200
    result['msg'] = []
    host = Host.objects.all().values()
    if(host.count()>0):
        for val in host:
            val['createtime'] = val['createtime'].strftime("%Y-%m-%d %H:%M:%S")
            # print(val)
            result['msg'].append(val)

    return HttpResponse(json.dumps(result), content_type="application/json")


