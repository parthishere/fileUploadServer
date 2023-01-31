from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to="log-file")
    
    def __str__(self):
        return str(self.pk)