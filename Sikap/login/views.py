from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from .models import *
#from .forms import *
# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request,'blogin.html')

    # def post(self,request):        
    #     user = request.POST.get("user")        
    #     password = request.POST.get("pass")
    #     q = Admin.objects.get(username = user)
    #     if q.password == password:
    #         return redirect('app:dashboard_view')
    #     else:
    #         return HttpResponse("User does not exist!")