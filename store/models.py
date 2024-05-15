from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
class Furniture(models.Model):
    CATEGORIES = (
        ('Sofa', 'Sofa'),
        ('Chair', 'Chair'),
        ('Table', 'Table'),
        ('Bed', 'Bed'),
        ('Home Appliance', 'Home Appliance')
    )
    IMAGES = (
        ('white-sofa.jpg', 'white-sofa.jpg'),
        ('kitchen-table.jpg', 'kitchen-table.jpg'),
        ('king-bed.jpg', 'king-bed.jpg'),
        ('toaster.jpg', 'toaster.jpg'),
        ('wooden-chair.jpg', 'wooden-chair.jpg')
    )
    name = models.CharField(max_length=255, null=True)
    
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    
    price = models.FloatField(null=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    furniture = models.ForeignKey(Furniture, null=True, on_delete=models.SET_NULL)
    soldBy = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=255, null=True, choices=STATUS)

    def __str__(self):
        return f'{self.furniture} - {self.customer.name}'

