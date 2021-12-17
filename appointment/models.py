from django.contrib.auth import get_user_model
from django.db import models


class Appointment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    appointee = models.ForeignKey(Appointee, on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=True)
    subject = models.CharField(max_length=200)
    is_pending = models.BooleanField(default=True)
    is_checked = models.BooleanField(default=False)


class Comment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField(null=True)
    date_time = models.DateTimeField(auto_now_add=True) 
