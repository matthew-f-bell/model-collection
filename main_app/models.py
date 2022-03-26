from django.db import models

# Create your models here.

GRADE_CHOICES = (
    ("SD", "SD Gundam"),
    ("MG", "Master Grade"),
    ("HG", "High Grade"),
    ("NG", "No Grade")
)

class FigureModels(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    brand = models.CharField(max_length=50)
    grade = models.CharField(max_length=20, choices = GRADE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']