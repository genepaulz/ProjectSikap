from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from login.models import *
from .forms import *
#from .forms import *
# Create your views here.
class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    # def post(self,request):        
    #     email = request.POST.get("email")        
    #     password = request.POST.get("pass")

    #     form = Applicant(
    #         email = email,
    #         password = password
    #     )
    #     form.save()
    #     return redirect('landing:landing_view')