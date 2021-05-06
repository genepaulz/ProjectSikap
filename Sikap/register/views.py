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

    def post(self,request):        
        if 'applicant' in request.POST:
                account_type = 1
                email = request.POST.get("aemail")
                password = request.POST.get("apassword")
                name = request.POST.get("aname")
                surname = request.POST.get("asurname")
                user_type = 0
                isVerified = 0
                industry = request.POST.get("aindustry")
                region = request.POST.get("aregion")
                province = request.POST.get("aprovince")
                city = request.POST.get("acity")
                age = request.POST.get("aage")
                print(account_type)
                print(email)
                print(password)
                print(name)
                print(surname)
                print(user_type)
                print(isVerified)
                print(industry)
                print(region)
                print(province)
                print(city)
                print(age)

                form = User(
                    account_type = account_type,
                    email = email,
                    password = password,
                    name = name,
                    surname = surname,
                    user_type = user_type,
                    isVerified = isVerified,
                    companyName = "",
                    industry = industry,
                    region = region,
                    province = province,
                    city = city,
                    age = age
                )
                form.save()                
                return redirect('landing:landing_view')

        elif 'employer' in request.POST:
                account_type = 1
                email = request.POST.get("eemail")
                password = request.POST.get("epassword")
                name = request.POST.get("ename")
                surname = request.POST.get("esurname")
                user_type = 1
                isVerified = 0
                companyName = request.POST.get("ecompanyName")
                industry = request.POST.get("eindustry")
                print(account_type)
                print(email)
                print(password)
                print(name)
                print(surname)
                print(user_type)
                print(isVerified)
                print(industry)

                form = User(
                    account_type = account_type,
                    email = email,
                    password = password,
                    name = name,
                    surname = surname,
                    user_type = user_type,
                    isVerified = isVerified,
                    companyName = companyName,
                    industry = industry,
                    region = "",
                    province = "",
                    city = "",
                    age = 0
                )
                form.save()
                return redirect('landing:landing_view')