from django.shortcuts import render,redirect,HttpResponse
from Registerusre.models import RegisterUser
from sleeper.models import Trainspecificdata


def Res(request):
    if request.method=='POST':
        companyname=request.POST.get('companyname')
        ownername=request.POST.get('ownername')
        rollno=request.POST.get('rollno')
        owneremail=request.POST.get('owneremail')
        accesscode=request.POST.get('accesscode')
        User=RegisterUser(companyname=companyname,ownername=ownername,rollno=rollno,owneremail=owneremail,accesscode= accesscode)
        User.save()
        return redirect('tr')
    return render(request,'register.html')

def Traindata(request):
    
    return render(request,'traininfo.html')

def sleeper_train_info(request):
    try:
        sleeper_train = Trainspecificdata.objects.get(trainName="express")
    except Trainspecificdata.DoesNotExist:
        sleeper_train = None

    context = {'sleeper_train': sleeper_train}
    return render(request, 'sleepertrain.html', context)