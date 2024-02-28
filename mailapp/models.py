from django.db import models


class contactus(models.Model):
    firstname = models.TextField(max_length=255)
    Lastname = models.TextField(max_length=255)
    email = models.EmailField(primary_key=True)
    comments = models.TextField(max_length=255)

    class Meta:
        db_table = "contactus"
# Create your models here.
