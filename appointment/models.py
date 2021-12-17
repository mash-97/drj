from django.db import models

from users.models import *


class Appointment(models.Model):
    appointee = models.ForeignKey(Appointee, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    appointed_datetime = models.DateTimeField(null=True)
    
