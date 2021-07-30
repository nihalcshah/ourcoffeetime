from django.db import models

# Create your models here.
class TestResults(models.Model):
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.description