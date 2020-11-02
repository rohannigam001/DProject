from django.db import models

# Create your models here.

class Wiki(models.Model):
    serial_no=models.FloatField(null=True, blank=True, default=None)
    sentence_id=models.FloatField(null=True, blank=True, default=None)
    source=models.CharField(max_length=122, default='0')
    destination=models.CharField(max_length=122, default='0')
    surface_name=models.CharField(max_length=122, default='0')
    correct=models.FloatField(null=True, blank=True, default=None)
    unique_source=models.CharField(max_length=122, default='0')
    

    def __str__(self):
        # return str(self.sentence_id)
        return self.source
