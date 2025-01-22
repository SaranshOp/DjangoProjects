from django.db import models
from django.utils import timezone # This is used to get the current date and time

# Create your models here.
class ChaiVariety(models.Model):

    CHAI_TYPE = (
        ('ML', 'Masala Latte'),
        ('CL', 'Chai Latte'),
        ('CH', 'Chai'),
        ('IC', 'Iced Chai'),
        ('EL', 'Elachi Chai'),
    )

    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='chai_images/') # This requires the Pillow library to be installed
    date_added = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE)
    description = models.TextField(default='') # This is a compulsory field therefore we need to provide a default value

    def __str__(self):
        return self.name