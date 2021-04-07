from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from .models import *
#from .forms import *
# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request,'blogin.html')

    def post(self,request):        
        email = request.POST.get("email")        
        password = request.POST.get("pass")
        isEmployer = 0
        try:
            q= Applicant.objects.get(email=email)
            isEmployer = 0
        except:
            isEmployer = 1
            q = Employer.objects.get(email=email)
        

        if q.password == password:
            return HttpResponse("Success")
        else:
            return HttpResponse("User does not exist!")
       