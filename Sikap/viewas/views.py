from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from .models import *
#from .forms import *
# Create your views here.
class ViewAsView(View):
    def get(self,request):
        return render(request,'viewas.html')