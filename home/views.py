from django.shortcuts import render
from django.http import HttpResponse

from .models import Department,Doctor
from .forms import BookingForm

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'confirmation.html')
    form = BookingForm()
    context={
        'form': form,
    }
    return render(request,'booking.html',context)

def department(request):
    instances = Department.objects.all()
    context ={
        'instances':Department.objects.all()
    }
    return render(request,'department.html',context=context)

def doctors(request):
    instances = Doctor.objects.all()
    context ={
        'doctors':instances
    }
    return render(request,'doctors.html',context)

def contact (request):
    return render(request,'contact.html')
