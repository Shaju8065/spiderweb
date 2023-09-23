from django.shortcuts import render
from .models import EmpOperations

# http://127.0.0.1:8000/spider
def index(request):
    return render(request,"index.html")


def newemp(request):
    return render(request,"NewEmployee.html")
    

# def addemp(request):
#     if request.method=="POST":
#         cstid=float(request.POST.get("cstId"))
#         cr=request.POST.get("cars")
#         csnm=request.POST.get("cstNm")
#         crnm=request.POST.get("carNm")
#         ctnm=request.POST.get("ctNm")
#         # call a processing funtion (models)
#         obj=EmpOperations()
#         stat=obj.addnewemployee(id, cr, csnm, crnm, ctnm)
#         dic={}
#         dic['cstid']=cstid
#         dic['car']=cr
#         dic['csnm']=csnm
#         dic['crnm']=crnm
#         dic['ctnm']=ctnm
#         dic['status']=stat
#     return render(request,"EmployeeAdded.html",dic)

def addemp(request):
    if request.method == "POST":
        cstid = float(request.POST.get("cstId"))
        cr = request.POST.get("cars")
        csnm = request.POST.get("cstNm")
        crnm = request.POST.get("carNm")
        ctnm = request.POST.get("ctNm")

        try:
            # Call a processing function (models) to add a new employee
            obj = EmpOperations()
            stat = obj.addnewemployee(cstid, cr, csnm, crnm, ctnm)
            status = 'success'
        except Exception as e:
            print(e)
            status = 'error'

        # Prepare a context dictionary to pass data to the template
        context = {
            'cstid': cstid,
            'car': cr,
            'csnm': csnm,
            'crnm': crnm,
            'ctnm': ctnm,
            'status': status,
        }

        return render(request, "EmployeeAdded.html", context)

    return render(request, "EmployeeAdded.html")


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