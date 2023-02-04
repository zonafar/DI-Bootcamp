from django.shortcuts import render,redirect
from django.utils import timezone
from rent.models import *
from rent.forms import rentalForm



def rental(request,pk):
    rental = Rental.objects.get(id=pk)
    return render(request,'rental/rental.html',{"rental":rental})
    
def rentals(request):
    rentals = Rental.objects.order_by('-rental_date')
    return render(request,'rental/rentals.html',{"rentals":rentals})

def rental_add(request):
    if request.method == "GET":
        form = rentalForm()
    if request.method == 'POST':
        form = rentalForm(request.POST)
        if form.is_valid():
            rental_date = form.cleaned_data.get('rental_date')
            return_date = form.cleaned_data.get('return_date')
            v_id = form.cleaned_data.get('vehicle')
            c_id = form.cleaned_data.get('customer') 
            customer = Customer.objects.get(id=c_id)
            vehicle = Vehicle.objects.get(id=v_id)
            rental = Rental(return_date = return_date,rental_date=rental_date,vehicle = vehicle,customer = customer)
            rental.save()
            vehicle.rented = True
            vehicle.save()
        return redirect('rent.rental', rental.id)
    return render(request, 'rental/rental_add.html', {'form':form})

 
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    print(customer.vehicles.first())
    raise Exception ("Stop")
    rental = customer.vehicles
    return render(request,'customer/customer.html',{"customer":customer,"rental":rental})

def customers(request):
    pass

def customer_add(request,pk):
    pass


def vehicle(request,pk):
    vehicle = Vehicle.objects.get(id=pk)
    return render(request,'vehicle/vehicle.html',{"vehicle":vehicle})

def vehicles(request):
    pass

def vehicle_add(request,pk):
    pass

def vehicle_return(request,pk):
    rental = Rental.objects.get(id=pk)
    rental.return_date = timezone.now()
    rental.vehicle.rented = False   
    rental.vehicle.save()
    rental.save()
    return redirect('rent.rentals')






