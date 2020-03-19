from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")



from common.models import Customer

# def listcustomers(request):
# 	#返回一个QuerySet 对象，包含所有的表记录
# 	#每条表记录都是一个dict对象
# 	#key是字段名，value是字段值
# 	qs = Customer.objects.values()    

# 	#定义返回字符串
# 	reStr = ''
# 	for customer in Customer:
# 		for name,value in customer.items():
# 			reStr += f'{name}:{value}|'

# 		#<br>表示换行
# 		retStr += '<br>'
# 	return HttpResponse(retStr)
# 	
# 	
# 	
# 	
# 过滤条件
def listcustomers(request):
	qs = Customer.objects.values()
	#检查url中是否有参数phonenumber
	ph = request.GET.get('phonenumber',None)
	#如果有，加过滤条件
	if ph:
		qs = qs.filter(phonenumber=ph)


		#定义返回字符串
	retStr = ''
	for customer in qs:
		for name,value in customer.items():
			retStr += f'{name}:{value}|'
		retStr += '<br>'
	return HttpResponse(retStr)




















