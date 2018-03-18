from django.db import models
from datetime import date
# Create your models here.
class Owners(models.Model):

    STATES_LIST = (
        ('punjab', 'Punjab'),)

    CITY_LIST = (
    ('jalandhar','Jalandhar'),)

    PARKING_LIST = (
    ('none','None'),
    ('bike','Bike'),
    ('car','Car'),
    ('both','Both'),)

    CC = (
    ('91','+91'),)

    APARTMENT_TYPE = (
    ('apartment','Apartment'),
    ('pg/hostel','PG/Hostel'),
    ('shop','Shop'))

    BHK_TYPE = (
    ('1','1BHK'),
    ('2','2BHK'),
    ('3','3BHK'),
    ('4','4BHK'),
    ('5','4+BHK'),)

    FACING = (
    ('e','East'),
    ('w','West'),
    ('n','North'),
    ('s','South'),
    ('ne','North East'),
    ('nw','North West'),
    ('se','South East'),
    ('sw','South West'),)

    FURNISHING = (
    ('full','Full'),
    ('semi','Semi'),
    ('no','Not Furnished'),)

    PREFFERED_TENANT = (
    ('family','Family'),
    ('bachelor','Bachelor'),
    ('anyone','Anyone'),)



    # fields below
    owners_name = models.CharField(max_length=50,blank=False)
    mail_id = models.EmailField(max_length=100,blank=True)
    country_code = models.CharField(
        max_length=50,
        choices=CC,
        default='+91',
        blank=False
    )
    phone = models.PositiveIntegerField(blank=False, unique=True)
    apartment_type = models.CharField(
        max_length=50,
        choices=APARTMENT_TYPE,
        blank=False
        )

    bhk_type = models.CharField(
        max_length=50,
        choices=BHK_TYPE,
        blank=False)

    property_size = models.CharField(max_length=150,blank=True)
    property_age = models.PositiveIntegerField(blank=True,null=False,default=0)
    facing = models.CharField(
        max_length=50,
        choices=FACING,
        blank=True
        )

    rented_floors = models.PositiveIntegerField(blank=False)
    total_floors = models.PositiveIntegerField(blank=False)
    expected_rent = models.PositiveIntegerField(blank=False)
    negotiable = models.BooleanField(default=False)
    expected_deposit = models.PositiveIntegerField(blank=False)
    available_from  = models.DateField(default=date.today,blank=False)
    furnishing = models.CharField(
        max_length=50,
        choices=FURNISHING,
        blank=False)

    parking = models.CharField(
    max_length=10,
    choices=PARKING_LIST,
    blank=False
    )
    preffered_tenant = models.CharField(
        max_length=50,
        choices=PREFFERED_TENANT,
        blank=False)

    address = models.CharField(max_length=500,blank=False,null=False,default='')
    locality = models.CharField(max_length=200)
    city = models.CharField(
        max_length=50,
        choices=CITY_LIST,
        default='jalandhar',
        blank=False
    )
    pincode = models.PositiveIntegerField(blank=True)
    state = models.CharField(
        max_length=50,
        choices=STATES_LIST,
        default='punjab',
        blank=False
    )
    property_description = models.TextField(blank=True)
    pics_from = models.PositiveIntegerField(blank=True)
    pics_till = models.PositiveIntegerField(blank=True)
    number_of_pics = models.PositiveIntegerField(blank=False)
    def __str__(self):
        return self.owners_name
