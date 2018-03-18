# Generated by Django 2.0 on 2018-03-18 04:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owners_name', models.CharField(max_length=50)),
                ('mail_id', models.EmailField(blank=True, max_length=100)),
                ('country_code', models.CharField(choices=[('91', '+91')], default='+91', max_length=50)),
                ('phone', models.PositiveIntegerField(unique=True)),
                ('apartment_type', models.CharField(choices=[('apartment', 'Apartment'), ('pg/hostel', 'PG/Hostel'), ('shop', 'Shop')], max_length=50)),
                ('bhk_type', models.CharField(choices=[('1', '1BHK'), ('2', '2BHK'), ('3', '3BHK'), ('4', '4BHK'), ('5', '4+BHK')], max_length=50)),
                ('property_size', models.CharField(blank=True, max_length=150)),
                ('property_age', models.PositiveIntegerField(blank=True, default=0)),
                ('facing', models.CharField(blank=True, choices=[('e', 'East'), ('w', 'West'), ('n', 'North'), ('s', 'South'), ('ne', 'North East'), ('nw', 'North West'), ('se', 'South East'), ('sw', 'South West')], max_length=50)),
                ('rented_floors', models.PositiveIntegerField()),
                ('total_floors', models.PositiveIntegerField()),
                ('expected_rent', models.PositiveIntegerField()),
                ('negotiable', models.BooleanField(default=False)),
                ('expected_deposit', models.PositiveIntegerField()),
                ('available_from', models.DateField(default=datetime.date.today)),
                ('furnishing', models.CharField(choices=[('full', 'Full'), ('semi', 'Semi'), ('no', 'Not Furnished')], max_length=50)),
                ('parking', models.CharField(choices=[('none', 'None'), ('bike', 'Bike'), ('car', 'Car'), ('both', 'Both')], max_length=10)),
                ('preffered_tenant', models.CharField(choices=[('family', 'Family'), ('bachelor', 'Bachelor'), ('anyone', 'Anyone')], max_length=50)),
                ('address', models.CharField(default='', max_length=500)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(choices=[('jalandhar', 'Jalandhar')], default='jalandhar', max_length=50)),
                ('pincode', models.PositiveIntegerField(blank=True)),
                ('state', models.CharField(choices=[('punjab', 'Punjab')], default='punjab', max_length=50)),
                ('property_description', models.TextField(blank=True)),
                ('pics_from', models.PositiveIntegerField(blank=True)),
                ('pics_till', models.PositiveIntegerField(blank=True)),
                ('number_of_pics', models.PositiveIntegerField()),
            ],
        ),
    ]
