"""Content Camera"""

# Libraries
from django.db import models

 # Modules


class Camera(models.Model):
    name = models.CharField("name", max_length=100, )

    def __str__(self):
        return f"Camera {self.pk}"

    def __repr__(self):
        return str(self)