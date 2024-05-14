from django.db import models


class Specialist(models.Model):
    SPECIALTY_CHOICES = [
        ('psychologist', 'Psychologist'),
        ('coach', 'Coach'),
        ('doctor', 'Doctor'),
        ('therapist', 'Therapist'),
        ('counselor', 'Counselor'),
        ('psychiatrist', 'Psychiatrist'),
        ('nutritionist', 'Nutritionist'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    specialty = models.CharField(max_length=100, choices=SPECIALTY_CHOICES)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='doctor_profiles/', blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"