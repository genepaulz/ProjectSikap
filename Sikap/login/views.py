from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from .models import *
from django.template import *
from .import views


#from .forms import *
# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email = request.POST.get("email")
        password = request.POST.get("pass")

        query_results = User.objects.filter(email=email)
        if (query_results):
            try:
                query_results = User.objects.get(email=email)
                if(query_results.password==password):
                    if(query_results.user_type==0):

                        #request.sessions['name'] = query_results ;
                        #print(q)
                        #return HttpResponse(q)
                        #return render(request,'viewasa_view')
                        return redirect('viewas:viewasa_view')
                    elif(query_results.user_type==1):
                        return redirect('viewas:viewase_view')
                else:
                    return HttpResponse("Fail")
            except:
                #print('Hello')

                return HttpResponse("User does not exist!")

                #def review_view(request, *args, **kwargs):