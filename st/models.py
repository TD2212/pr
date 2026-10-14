
from django.db import models

class student(models.Model):
    S_id = models.AutoField(primary_key=True)
    S_name = models.CharField(max_length=100)
    S_email = models.EmailField()
    S_mobile = models.CharField(max_length=15)
    S_city = models.CharField(max_length=100)

    def __str__(self):
        return str(self.S_id)

