# import  requests,pprint

# response = requests.get('http://localhost/mgr/medicine?action=list_customer')

# pprint.pprint(response.json())




import  requests,pprint

response = requests.post('http://localhost/mgr/signin?username=chao&password=01234578')
# 构建添加 客户信息的 消息体，是json格式

# payload = {
#     "action":"add_order",
#     "data":{
#         "name":"华山医院订单002",
#         "customerid":3,
#         "medicineids":[1,2]
#     }
# }

# # 发送请求给web服务
# response = requests.post('http://localhost/mgr/orders',
#               json=payload)

# pprint.pprint(response.json())

# # 构建查看 客户信息的消息体
# response = requests.get('http://localhost/mgr/orders?action=list_customer')

# 发送请求给web服务
pprint.pprint(response.json())