from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from .models import *
#from .forms import *
# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):        
        email = request.POST.get("email")        
        password = request.POST.get("pass")
        
        q = User.objects.filter(email=email)
        if (q):
            try:
                q = User.objects.get(email=email)
                if(q.password==password):
                    return HttpResponse("Success")
                else:
                    return HttpResponse("Fail")
            except:
                return HttpResponse("User does not exist!")