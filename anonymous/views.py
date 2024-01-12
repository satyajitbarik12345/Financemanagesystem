from django.shortcuts import redirect ,render
from anonymous.models import Employees

# Create your views here.

def index(request):
    emp = Employees.objects.all()

    context = {
        'emp':emp,
    }
    return render(request,'index.html',context)
def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        dateofexpense = request.POST.get('dateofexpense')
        amount = request.POST.get('amount')
        updatedat = request.POST.get('updatedat')
        createdby = request.POST.get('createdby')

        emp = Employees(
            name = name,
            category = category,
            dateofexpense = dateofexpense,
            amount = amount,
            updatedat = updatedat,
            createdby = createdby, 
        )
        emp.save()
        return redirect('home')

    return render(request,'index.html')
def Edit(request):
    emp = Employees.objects.all()
    context = {
        'emp':emp,
    }
    return redirect(request,'index.html',context)

def update(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        dateofexpense = request.POST.get('dateofexpense')
        amount = request.POST.get('amount')
        updatedat = request.POST.get('updatedat')
        createdby = request.POST.get('createdby')
        emp = Employees(
            id = id,
            name = name,
            category = category,
            dateofexpense = dateofexpense,
            amount = amount,
            updatedat = updatedat,
            createdby = createdby, 
        )
        emp.save()
        return redirect('home')
    return redirect(request,'index.html')

def Delete(request,id):
    emp = Employees.objects.filter(id=id)
    emp.delete()
    context = {
        'emp':emp,
    }
    return redirect('home')









