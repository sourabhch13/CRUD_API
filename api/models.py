from django.db import models
import uuid

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=50, unique=True)
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)

    description=models.TextField(blank=True)

    def __str__(self):
        return self.name