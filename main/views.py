from django.shortcuts import render,HttpResponseRedirect
from main.form import StudentForm
from main.models import Student
from django.views.generic.base import TemplateView,RedirectView
from django.views import View

# Create your views here.

class Addshow(TemplateView):
    def get(self,request):
        students=Student.objects.all()
        form=StudentForm()
        context={'form':form,'students':students}
        return render(request,'main/base.html',context) 
    
    def post(self,request):
        fm=StudentForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            rollno=fm.cleaned_data['rollno']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            new=Student(name=name,rollno=rollno,email=email,password=password)
            new.save()
            return HttpResponseRedirect('/')
            


class delete1(RedirectView):
    url='/'
    def get_redirect_url(self,*args,**kwargs):
        id=kwargs['id']
        Student.objects.get(pk=id).delete()
        return super().get_redirect_url()

class Update(TemplateView):
    template_name='update.html'
    def get(self,request,id):
        pi=Student.objects.get(pk=id)
        fm=StudentForm(instance=pi)
        context={"fm":fm}
        return render(request,'main/update.html',context)
    def post(self,request,id):
        pi=Student.objects.get(pk=id)
        fm=StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        context={"fm":fm}
        return render(request,'main/update.html',context)







        


