from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.
def index(request):
    username=request.GET.get('username')
    if username:
       return HttpResponse("后台首页")
    else:
        current_namespace=request.resolver_match.namespace
        print(current_namespace)
        return redirect(reverse("%s:login" % current_namespace))
       # login_url=reverse('cms:login')
       # print("="*50)
       # print(login_url)
       # print("="*50)
       # return redirect(login_url)

       # return redirect(reverse('cms:login'))
def login(request):
    return HttpResponse("后台登录首页")