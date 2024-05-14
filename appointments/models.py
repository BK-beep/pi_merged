from django.db import models
from specialists.models import Specialist
from users.models import User

class Appointment(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_datetime = models.DateTimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment with {self.specialist.name} on {self.appointment_datetime}"
