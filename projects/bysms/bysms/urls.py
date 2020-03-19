"""bysms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""





# 静态文件服务
from django.conf.urls.static import static
from django.urls import path,include
from django.contrib import admin
from sales.views import listorders

urlpatterns = [
    path('admin/', admin.site.urls),
    #凡是url以sales/ 开头，都是根据sales.urls里面的子路由表进行路由
    path('sales/', include('sales.urls')),
    #凡是url 以api/mgr开头的，根据mgr.urls里面的子路由表进行
    path('api/mgr/', include('mgr.urls')),
]+  static("/", document_root="./z_dist")
