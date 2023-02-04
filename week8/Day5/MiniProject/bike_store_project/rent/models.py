from django.db import models
from django.utils import timezone

from datetime import datetime
from faker import Faker
import random



class Customer(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 30)
    address = models.CharField(max_length = 30)
    city = models.CharField(max_length = 40)
    country = models.CharField(max_length = 100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def name(self):
        return f"{self.first_name} {self.last_name}"

    # def present_rental(self):
    #     rentals = self.vehicles.objects.first()
    #     return rentals

class Vehicle_Size(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name

class Vehicle_Type(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name

# ‘bike’, ‘electric bike’, ‘scooter’, ‘jetpack’,
# small’, ‘medium’, ‘large’, ‘double’

#sb: 4.99 , seb=5.99 , ss=6.99 sj=9.99
#mb: 5.49 , meb=10.99 , ms=12.99 sj=14.99
#lb: 7.49 , leb=11.99 , ls=14.99 lj=16.99
#db: 7.99 , deb=13.99 , ds=15.99 lj=19.99

class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=100)
    date_created  = models.DateField(default = timezone.now())
    real_cost = models.FloatField()
    rented = models.BooleanField(default=False)
    size = models.ForeignKey(Vehicle_Size,on_delete = models.CASCADE, related_name = "sizes")
    def __str__(self):
        return f'{self.vehicle_type}'

    #Vehicle.objects.create(vehicle_type = fake.file_name(),real_cost = fake.pyfloat(left_digits=5,right_digits=2,positive=True),size = random.choice(Vehicle_Size.objects.all()))

    def generate_vehicle():
        fake = Faker()
        sizes=Vehicle_Size.objects.all()

        type = fake.file_name()
        cost = fake.pyfloat(right_digits=2,positive=True)
        size = random.choice(sizes)
        vehicle = Vehicle(vehicle_type = type,real_cost = cost,size = size)
        vehicle.save()
        return vehicle

class Rental(models.Model):
    rental_date = models.DateField(default = timezone.now())
    return_date = models.DateField(null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name="customers")
    vehicle = models.ForeignKey(Vehicle, on_delete = models.CASCADE, related_name="vehicles" )


    def __str__(self):
        return f'{self.rental_date} - {self.return_date}' 

    def return_date_well(self):
        if self.return_date == None:
            return ""
        return self.return_date

    def generate_rental(): 
        fake = Faker()
        customers = Customer.objects.all()
        vehicles = Vehicle.objects.all()

        rental_date = fake.date_time_this_year() 
        while rental_date > datetime.today(): # Be sure that rental date not in future
            rental_date = fake.date_time_this_year()
        
        end_rand = random.randint(0,100) 
        return_date1 = fake.date_between(start_date = rental_date, end_date=f'+{end_rand}d') #return date (if not null) must be after rental date
        return_date = random.choice([None,return_date1]) #return date should sometimes be null

        vehicle = random.choice(vehicles)
        while vehicle.rented == True: #if a vehicle is already rented and has not been returned, it should not be used for a new rental.
            vehicle =  random.choice(vehicles)

        rental = Rental(rental_date = rental_date, return_date= return_date,customer = random.choice(customers),vehicle =vehicle)
        rental.save()

        if rental.return_date == None:
            vehicle.rented = True # Notified that vehicle has been rented
        vehicle.save()
        return rental

class Rental_Rate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type  = models.ForeignKey(Vehicle_Type, on_delete = models.CASCADE, related_name="vehicle_types")
    vehicle_size  = models.ForeignKey(Vehicle_Size, on_delete = models.CASCADE, related_name="vehicle_sizes")

    def __str__(self):
        return f'{self.daily_rate}'


 