from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login")
def Home(request):
    return render(request,'Home.html')

@login_required(login_url="/login")
def book(request):
    global roomuser
    
    if request.method=='POST' and 'bkbtn' in request.POST:
        roomdata=Booking(
            r_type=request.POST['room_type'],
            r_no=request.POST['rno'],
            r_dfrom=request.POST['Dfrom'],
            r_dto=request.POST['Dto'],
            r_payment=request.POST['payment'],
            r_unm=roomuser
        )
        roomdata.save()

    return render(request,'book.html')

@login_required(login_url="/login")
def Dining(request):
    return render(request,'Dining.html')

@login_required(login_url="/login")
def room(request):
    return render(request,'room.html')

@login_required(login_url="/login")
def AboutUs(request):
    context={'name':"Mr. X",'sname':'Y','marks':[100,99,100,99]}
    return render(request,'AboutUs.html',context)

@login_required(login_url="/login")
def showalldata(request):
    data=[{'eid':1001,'name':'Raj','mob':'123','email':'xyz.com'}
    ,{'eid':1002,'name':'Ram','mob':'456','email':'jkl.com'}
    ,{'eid':1003,'name':'Taj','mob':'789','email':'abc.com'}
    ,{'eid':1003,'name':'Maharaj','mob':'987','email':'efg.com'}
    ]
    context={'userdata':data}
    return render(request,'showalldata.html',context)

roomuser=""
def Login(request):
    if request.method=='POST' and 'lgbtn' in request.POST:
        unm=request.POST.get('uname')
        global roomuser
        roomuser=unm
        pwd=request.POST.get('password')
        user=authenticate(request,username=unm,password=pwd)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/home')
        else:
            msg="Invalid credentials***"
            return render(request,'login.html',{'err':msg})
    return render(request,'login.html')
               

def practice(request):
    res = 0
    if request.method=='POST' and 'addbtn' in request.POST:
       res=int(request.POST.get('num1'))+int(request.POST['num2'])
       print("Sum", res)
    return render(request, 'practice.html',{"r":res})

def register(request):
    if request.method=='POST' and 'regbtn' in request.POST:
        udata=UserData(
            user_name=request.POST['uname'],
            user_pwd=request.POST['password'],
            user_email=request.POST['email'],
            user_mob=request.POST['mob'],
        )
        udata.save()
        # enm=request.POST['ename']
        # print(enm)

    return render(request,'register.html')

@login_required(login_url="/login")
def ShowRecords(request):
    global roomuser
    if request.method=='POST' and 'showbtn' in request.POST:
        roomdata=Booking.objects.filter(r_unm=roomuser).values()#select * from database
        return render(request,'show.html', {"roomdata": roomdata })
    return render(request,'show.html')

@login_required(login_url="/login")
def Contact(request):
    # if request.method=='POST' and 'showbtn' in request.POST:
        employeedata=EmployeeData.objects.all().values()
    #     print(employeedata)
        return render(request,'Contact.html',{'employeedata':employeedata})
    # return render(request,'Contact.html')

@login_required(login_url="/login")
def edit(request, id):
    if request.method=='POST' and 'upbtn' in request.POST:
        employeedata=EmployeeData.objects.get(id=id)
        employeedata.emp_pwd=request.POST.get('password')
        employeedata.save()
        return HttpResponseRedirect('/show')
    employeedata=EmployeeData.objects.get(id=id)
    return render(request,'edit.html', {"employeedata":employeedata})


def user_reg(request):
    if request.method=='POST' and 'regbtn' in request.POST:
        pwd=request.POST.get('password')
        rpwd=request.POST.get('repassword')
        if(pwd==rpwd):
            user=User.objects.create_user(
                username=request.POST.get("uname"),
                password=request.POST.get("password"),
                email=request.POST.get("email")
                )
            user.save()
            return HttpResponseRedirect('/')
        else:
            msg="Password mismatched"
            return render(request,'user_reg.html',{'err':msg})
    return render(request,'user_reg.html')
@login_required(login_url="/login")
def Logout(request):
    logout(request)
    return HttpResponseRedirect("/")
    