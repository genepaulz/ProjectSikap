from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from .models import *
from .forms import *
#from .forms import *
# Create your views here.
class PostsView(View):
    def get(self,request):
        return render(request,'createpost.html')

    def post(self,request):        
        yearsOfExperience = request.POST.get("yearsOfExperience")
        industry = request.POST.get("industry")
        region = request.POST.get("region")
        province = request.POST.get("province")
        city = request.POST.get("city")
        age = request.POST.get("age")
        isAgeViewable = request.POST.get("isAgeViewable")
        if isAgeViewable == 'on':
            isAgeViewable = 1
        else:
            isAgeViewable = 0

        form = Posts(
            yearsOfExperience = yearsOfExperience,
            industry = industry,
            region = region,
            province = province,
            city = city,
            age = age,
            dateadded = datetime.now(),
            # EMAIL TO BE IMPLEMENTED WHEN WE HAVE SESSIONS
            isAgeViewable = isAgeViewable
        )
        form.save()
        return redirect('posts:posts_view')