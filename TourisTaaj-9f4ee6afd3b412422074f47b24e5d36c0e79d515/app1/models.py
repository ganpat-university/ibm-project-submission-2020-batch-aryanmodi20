from django.db import models

class Registration(models.Model):
    username = models.CharField(max_length=100)
    yearly_avg_view = models.IntegerField()
    frequentflyer = models.BooleanField()
    preferred_device = models.CharField(max_length=10, choices=[
        ('mobile', 'Mobile'),
        ('tablet', 'Tablet'),
        ('laptop', 'Laptop'),
        ('desktop', 'Desktop'),
    ])
    yearly_avg_outstation_checkins = models.IntegerField()
    annual_income_class = models.CharField(max_length=10, choices=[
        ('Average', 'Average'),
        ('High', 'High'),
        ('Low', 'Low'),
    ])
    member_in_family = models.IntegerField()
    booking_hotel = models.BooleanField()
    preferred_location_type = models.CharField(max_length=200)
    working_flag = models.BooleanField()
    travelling_rating = models.IntegerField()

    def __str__(self):
        return self.username