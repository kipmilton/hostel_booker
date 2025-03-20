from django.db import models
from django.contrib.auth.models import User

class Hostel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    hostel_type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    available_spaces = models.IntegerField()

    def __str__(self):
        return self.name




class HostelApplication(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    HOSTEL_TYPE_CHOICES = [
        ('Single Room', 'Single Room'),
        ('Double Room', 'Double Room'),
        ('Triple Room', 'Triple Room'),
        ('Quadruple Room', 'Quadruple Room'),
        ('Quintuple Room', 'Quintuple Room'),
        ('Sextuple Room', 'Sextuple Room'),
    ]

    LOCATION_CHOICES = [
        ('On-campus', 'On-campus'),
        ('Off-campus', 'Off-campus'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Allocated', 'Allocated'),
    ]

    YEAR_OF_STUDY_CHOICES = [
        ('Year One', 'Year One'),
        ('Year Two', 'Year Two'),
        ('Year Three', 'Year Three'),
        ('Year Four', 'Year Four'),
        ('Year Five', 'Year Five'),
        ('Year Six', 'Year Six'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=50, unique=True)
    year_of_study = models.CharField(max_length=20, choices=YEAR_OF_STUDY_CHOICES)  
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    hostel_type = models.CharField(max_length=20, choices=HOSTEL_TYPE_CHOICES)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    hostel_name = models.CharField(max_length=100)
    cost_per_semester = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.name} - {self.hostel_name}"




class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=HostelApplication.GENDER_CHOICES)
    registration_number = models.CharField(max_length=50)
    date_booked = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Confirmed", "Confirmed")], default="Pending")

    def __str__(self):
        return f"{self.user.username} - {self.hostel.name}"






# class HostelApplication(models.Model):
#     GENDER_CHOICES = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     ]
    
#     HOSTEL_TYPE_CHOICES = [
#         ('Single Room', 'Single Room'),
#         ('Double Room', 'Double Room'),
#         ('Triple Room', 'Triple Room'),
#         ('Quadruple Room', 'Quadruple Room'),
#         ('Quintuple Room', 'Quintuple Room'),
#         ('Sextuple Room', 'Sextuple Room'),
#     ]

#     LOCATION_CHOICES = [
#         ('On-campus', 'On-campus'),
#         ('Off-campus', 'Off-campus'),
#     ]

#     STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('Allocated', 'Allocated'),
#     ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     reg_number = models.CharField(max_length=50, unique=True)
#     year_of_study = models.IntegerField()
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
#     hostel_type = models.CharField(max_length=20, choices=HOSTEL_TYPE_CHOICES)
#     location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
#     hostel_name = models.CharField(max_length=100)
#     cost_per_semester = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

#     def __str__(self):
#         return f"{self.name} - {self.hostel_name}"
