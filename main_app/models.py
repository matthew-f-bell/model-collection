from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Paint(models.Model):
    color = models.CharField(max_length=75)
    paint_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

GRADE_CHOICES = (
    ("SD", "SD Gundam"),
    ("MG", "Master Grade"),
    ("HG", "High Grade"),
    ("NG", "No Grade")
)

class Figure(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    brand = models.CharField(max_length=50)
    grade = models.CharField(max_length=20, choices = GRADE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paints = models.ManyToManyField(Paint)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']