from django.shortcuts import render
from .models import EmpOperations

# http://127.0.0.1:8000/spider
def index(request):
    return render(request,"index.html")


def newemp(request):
    return render(request,"NewEmployee.html")
    

def addemp(request):
    if request.method=="POST":
        nm=request.POST.get("enm")
        dp=request.POST.get("dept")
        ps=request.POST.get("post")
        sl=float(request.POST.get("sal"))
        # call a processing funtion (models)
        obj=EmpOperations()
        stat=obj.addnewemployee(nm,dp,ps,sl)
        dic={}
        dic['name']=nm
        dic['dept']=dp
        dic['post']=ps
        dic['salary']=sl
        dic['status']=stat
    return render(request,"EmployeeAdded.html",dic)


def empreport(request):
    obj=EmpOperations()
    data=obj.getreportdata()
    return render(request,"EmpReport.html",{"list":data})


def newworker(request):
    return render(request,"NewWorker.html")

def addworker(request):
    status=None
    dic={}
    if request.method=="POST":
        wid=request.POST.get("wid")
        wnm=request.POST.get("wnm")
        dep=request.POST.get("dep")
        pst=request.POST.get("pst")
        loc=request.POST.get("loc")
        sal=float(request.POST.get("sal"))
        
        obj=EmpOperations()
        status=obj.addnewworker(wid,wnm,dep,pst,loc,sal)
        dic['status']=status

    return render(request,"WorkerAdded.html",dic)

def showworkers(request):
    obj=EmpOperations()
    dic=obj.allworkers()
    return render(request,"ShowWorkers.html",dic)