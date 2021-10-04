from django.db import models

# Create your models here.


class Person(models.Model):
    GENDER_CHOICES = (
        (1, '男'),
        (0, '女')
    )

    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField(choices=GENDER_CHOICES)
    id_card = models.CharField(max_length=18)
    address = models.CharField(max_length=255)
    temperature = models.FloatField()

    class Meta:
        permissions = ()
