
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_customer      = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    email            = models.CharField(max_length=100)
    first_name       = models.CharField(max_length=100)
    last_name        = models.CharField(max_length=100)

class Customer(models.Model):
    user            = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number    = models.CharField(max_length=20)
   
    def __str__(self):
        return self.user.username
    

class Receptionist (models.Model):
    user             = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number     = models.CharField(max_length=20)
    

    def __str__(self):
        return self.user.username


class contact (models.Model):
    name        = models.CharField(max_length=100)
    email       = models.CharField(max_length=100)
    subject     = models.CharField(max_length=100)
    message     = models.TextField()

    def __str__(self):
        return self.subject


class Room (models.Model):
    CATEGORIES = (
        ('Home','Home'),
        ('Hotel','Hotel'),
        ('Cottage','Cottage')
    )

    NUMBER = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12')

    )

    TYPE = (
        
        ('Studio','Studio'),
        ('Single','Single'),
        ('Double','Double'),
        ('Triple','Triple'),
        ('Executive Suite','Executive Suite'),
        
    )
    host               = models.CharField(max_length=100, null=True)
    price              = models.FloatField(max_length=6, null=True)  
    details            = models.CharField(max_length=100, null=True)
    location           = models.CharField(max_length=100, null=True)
    amenities          = models.CharField(max_length=100, null=True)
    room_type          = models.CharField(max_length=100, null=True,choices= TYPE)
    room_style         = models.CharField(max_length=100, null=True)
    room_number        = models.CharField(max_length=100, null=True)
    rental_type        = models.CharField(max_length=100, null=True,choices= CATEGORIES)
    guest_capacity     = models.IntegerField(null=True,)
    number_of_beds     = models.IntegerField(null=True,)
    number_of_baths    = models.IntegerField(null=True,)
    number_of_bedrooms = models.IntegerField(null=True)
    kitchen            = models.ImageField( null=True, blank=True, upload_to = "images/")
    bathroom           = models.ImageField( null=True, blank=True, upload_to = "images/")
    profile            = models.ImageField( null=True, blank=True, upload_to = "images/")
    

    def __str__(self):
        return self.host


 

class reservation (models.Model):
    STATUS = (
        
        ('Reserved','Reserved'),
        ('Canceled','Canceled'),

    )
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id     = models.ForeignKey(Room,  on_delete=models.CASCADE)
    check_in    = models.DateField()
    check_out   = models.DateField()
    status      = models.BooleanField(choices=STATUS)
    


    def __str__(self):
        return self.name

    @property
    def date_diff(self):
        return (self.check_in - self.check_out).days 

