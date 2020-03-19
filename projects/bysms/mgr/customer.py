from django.http import JsonResponse
from django.http import HttpResponse
import json
# 导入 Customer 
from common.models import Customer




def dispatcher(request):
    #对顾客信息进行处理时，先进行sessionid的检查
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret':302,
            'msg':'未登录',
            'redirect':'/mgr/sign.html'},
            status=302)
    if request.session['usertype']!='mgr':
        return JsonResponse({
            'ret':302,
            'msg':'用户非msg类型',
            'redirect':'/mgr/sign.html'},
            status=302)
    



    # 将请求参数统一放入request 的 params 属性中，方便后续处理
    # return HttpResponse('h')
    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST','PUT','DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_customer':
        return listcustomers(request)
    elif action == 'add_customer':
        return addcustomer(request)
    elif action == 'modify_customer':
        return modifycustomer(request)
    elif action == 'del_customer':
        return deletecustomer(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)
    #加上cookie校验
    
    return JsonResponse({'ret': 0, 'retlist': retlist})


def addcustomer(request):
    info = request.params['data']
    #从请求消息中获取客户信息，并插入数据库中，返回值就是插入对象
    record = Customer.objects.create(name = info['name'],
                                    phonenumber = info['phonenumber'],
                                    address = info['address'])

    return JsonResponse({'ret':0,'id':record.id})

def modifycutomer(request):
    #找到该客户，并对其进行修改
    customerid = request.params['id']
    newdata = request.params['newdata']


    try:
        #根据id在数据库中找到相应的客户记录
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return {
                'ret':1,
                'msg':'id为' + str(custmoerid) + '的客户不存在'
        }

    if 'name' in newdata:
        customer.name = newdata['name']
    if 'phonenumber' in newdata:
        customer.phonenumber = newdata['phonenumber']
    if 'address' in newdata:
        customer.address = newdata['address']


    #注意，一定要执行save才能将修改信息保存到数据库
    customer.save()
    return JsonResponse({'ret':0})
def deletecustomer(request):
    customerid = request.params[id]
    try:
        #根据id从数据库中找到相应的客户记录
        customer = Customer.objects.get(id = customerid)
    except Customer.DoesNotExist:
        return {
                'ret':1,
                'msg':'id为' + str(custmoerid) + '的客户不存在'               
        }
        #delete方法就将该记录从数据库中删除
    customer.delete()
    return JsonResponse({'ret':0})    

























