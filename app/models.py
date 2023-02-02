from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class File(models.Model):
    file = models.FileField(upload_to="log-file")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.pk)
